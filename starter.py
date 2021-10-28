from webscraping import scrape
import mongo
import exceptions


try:
    instance = scrape()
    print(type(instance))
    instance.song_status = instance.connectToURL()
    mongo.run_databse()
except exceptions.connection_error as err:
    print("Connection Error : ",err)
except Exception as e:
    print("exception Detected -->  ", e)

