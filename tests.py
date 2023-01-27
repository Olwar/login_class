from login_class import Client

# tests
def test_main():
    right_uri_list = ["visma-identity://login?source=severa", "visma-identity://sign?source=vismasign&documentid=105ab44", "visma-identity://confirm?source=netvisor&paymentnumber=102226"]
    for uri in right_uri_list:
        print(uri)
        client = Client(uri)
        print("scheme:", client.get_scheme())
        print("path:", client.get_path())
        print("parameters:", client.get_parameter())
        print("message:", client.get_all())
        print("\n")

    wrong_uri_list = ["what what", 123123, "WRONG-IDENTITY://login?source=severa", "visma-identity://MACGYVER?source=vismasign&documentid=105ab44", "visma-identity://confirm?source=netvisor&paymentnumber=NOT-A-NUMBER"]
    for uri in wrong_uri_list:
        print(uri)
        try:
            client = Client(uri)
            print("scheme:", client.get_scheme())
            print("path:", client.get_path())
            print("parameters:", client.get_parameter())
            print("error:", client.get_all())
            print("\n")
        except:
            print("error in the uri")
            print("\n")

if __name__ == "__main__":
    test_main()
