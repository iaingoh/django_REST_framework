## Django Rest Framework

This Django project consists of one app that loads a json data file, saves it to model, and then exposes it as an endpoint via an api.

----
### Django
- Django must be installed for this project to run via it's built in development server.

### Routes
- Two routes are loaded:
   - dev/
   - call_data/

The dev route loads the included json file that's hardcoded into the view. The call_data route is pretty self-explanatory in that it calls the data via that API and that lists it through Rest Framework interface.

### The Json file being loaded
- 'doctype_data.json' consists of dummy data.
- List of dict type objects.
   - Two key, value pairs -> name, total_docs.
- Besides loading and saving the file contents, the view also returns a HttpResponse type stating that the view is loaded and returns the database entry count.

### Django Rest Framework
- Upon calling call_data, an interface will return, listing the entries.
- There are certain options to choose from including the format the data is being returned in.
- To serialize the database object, to convert that object into string, for listing purposes,

```
class DataList(APIView):

    def get(self, request):
        data_point = JDP.objects.all()
        serializer = DataSerializer(data_point, many=True)
        return Response(serializer.data)

```
