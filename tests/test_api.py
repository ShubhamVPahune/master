import pytest
import requests
import operations

class TestApi():

    def test_get_api(self):
        """"""
        en_url = "https://thesaurus.altervista.org/thesaurus/v1"
        req_params = {
            "output":"json",
            "language":"en_US",
            "word":"war",
            "key":"test_only"}
        
        response = requests.get(url=en_url, params=req_params)
        # assert response.status_code == 200, "Expected status code does not match"
        if response.status_code == 200:
            print("200")

            synonyms = [response.get("list").get("synonyms") for response in response.json().get("response")]
            print(synonyms)
        elif response.status_code == 403:
            print("403")
            raise Exception("Got 403 Status code for api")
        
    def test_learn_generator(self):
        gen = operations.sqr_generator()
        # print(f"gen = {gen}")
        # print(next(gen)) 
        # print(next(gen)) 
        # gen.send(5)
        print(gen.__next__())
        gen.__next__()
        gen.__next__()
        gen.__next__()
        for i in gen:
            print(i)
        #     gen.send(3)
        #     gen.throw(BaseException)
        #     gen.close()
            
    def test_verify_iterator(self):

        sqr = operations.SQUARE()
        # print(sqr.__next__())

        # print(next(sqr))

        print("\n")
        for i in sqr:
            print(i)

    def test_first_class_objects(self):
        print(f"sqr_generator doc string = {operations.sqr_generator.__doc__}")

    