import requests
import money_converter
import pprint

class travel():
    def country_deets(self,ctry):
        base_path="https://restcountries.eu/rest/v2"
        uri="/name/"
        srch_ctry=ctry
        query="fullText=true"
        r=requests.get(base_path+uri+srch_ctry+"?"+query)

        if r.status_code in range(200,300):
            #print("search success")
            #pprint.pprint(r.json())
            return r.json()
        else:
            print("API server GET fail")


class assistant():
    def say_hi(self):
        print("Hello Folks, I'm happy to help you" )

class travel_assistant(travel,assistant):

    def __init__(self,source,dest):
        self.source=source
        self.dest=dest

    def dest_details(self):
        return self.country_deets(self.dest)

    def source_details(self):
        return self.country_deets(self.source)

    def comp_src_to_dest(self):
        src_deets = self.source_details()
        dst_deets = self.dest_details()
        #print(dst_deets,"\n",src_deets)
        print("1. Book a flight between %s and %s"%(src_deets[0]['capital'],dst_deets[0]['capital']))
        print("2. Once you reach there, you'll meet %s immigration"%dst_deets[0]['demonym'])

if __name__ == '__main__':
    t=travel_assistant("india","Canada")
    t.comp_src_to_dest()
