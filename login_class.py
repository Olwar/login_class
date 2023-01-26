import re

# Example1: visma-identity://login?source=severa
# Example2: visma-identity://sign?source=vismasign&documentid=105ab44
# Example3: visma-identity://confirm?source=netvisor&paymentnumber=102226

class Identity:

    def __init__(self, uri):
        # regex to get everything before :
        self.scheme = re.search(r'^(.*):', uri).group(1)
        # regex to get everything after // and before ?
        self.path = re.search(r'(?<=//)(.*?)(?=\?)', uri).group(1)
        # regex to get everything after ? until the end of the string or until &
        self.parameter = re.search(r'(?<=\?)(.*?)(?=&|$)', uri).group(1)
        # if statment to see if there is a & in the uri
        if '&' in uri:
            # regex to get everything after & until =
            self.query = re.search(r'(?<=&)(.*?)(?==)', uri).group(1)
            # regex to get everything after documentid= or paymentnumber=
            self.query_value = re.search(r'(?<=\=)[^&]*$', uri).group()

    def check_scheme(self):
        if self.scheme == 'visma-identity':
            pass
        else:
            return "Wrong scheme"
    
    def check_path(self):
        if self.path in ("login", "confirm", "sign"):
            pass
        else:
            return "Wrong path"
        
    def check_parameter(self):
        return_dict = {}
        if self.path == "login":
            if self.parameter == "source=severa":
                pass
        elif self.path == "confirm":
            if self.parameter == "source=netvisor":
                if self.query == "paymentnumber":
                    # regex to separate get parameter after =
                    source_value = re.search(r'(?<==)(.*)', self.parameter).group(1)
                    return_dict["source"] = source_value
                    return_dict["paymentnumber"] = self.query_value
                    pass
        elif self.path == "sign":
            if self.parameter == "source=vismasign":
                if self.query == "documentid":
                    # regex to separate get parameter after =
                    source_value = re.search(r'(?<==)(.*)', self.parameter).group(1)
                    return_dict["source"] = source_value
                    return_dict["documentid"] = self.query_value
        else:
            return "Wrong parameter"
        return return_dict

    def identity_check(self):
        if self.check_scheme() == "Wrong scheme":
            return "Wrong scheme"
        elif self.check_path() == "Wrong path":
            return "Wrong path"
        res_dict = self.check_parameter()
        if res_dict == "Wrong parameter":
            return "Wrong parameter"
        else:
            return self.path, res_dict        
    
class Client:
    def __init__(self, uri):
        self.identity = Identity(uri)
        self.identity.identity_check()

    def get_scheme(self):
        return self.identity.scheme

    def get_path(self):
        return self.identity.path

    def get_parameter(self):
        return self.identity.parameter
    
    def get_all(self):
        return self.identity.identity_check()


def test_main():
    right_uri_list = ["visma-identity://login?source=severa", "visma-identity://sign?source=vismasign&documentid=105ab44", "visma-identity://confirm?source=netvisor&paymentnumber=102226"]
    for uri in right_uri_list:
        print(uri)
        client = Client(uri)
        print("scheme:", client.get_scheme())
        print("path:", client.get_path())
        print("parameters:", client.get_parameter())
        print("all:", client.get_all())
        print("\n")

    wrong_uri_list = ["WRONG-IDENTITY://login?source=severa", "visma-identity://MACGYVER?source=vismasign&documentid=105ab44", "visma-identity://confirm?source=netvisor&paymentnumber=NOT-A-NUMBER"]
    for uri in wrong_uri_list:
        print(uri)
        client = Client(uri)
        print("scheme:", client.get_scheme())
        print("path:", client.get_path())
        print("parameters:", client.get_parameter())
        print("all:", client.get_all())
        print("\n")

if __name__ == "__main__":
    test_main()
