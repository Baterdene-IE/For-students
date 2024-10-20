data = [{
    "FirstName": "Baterdene", "LastName": "Enkhkhudulmur", "Job": "Senior Engineer"
},
{
    "FirstName": "Khulan", "LastName": "Batdorj", "Job": "Marketing Manager"
}]
class People:
    msg = {"nodata": "Үр дүн байхгүй байна"}
    def __init__(self, data):
        self.data = data
    def get(self, kwargs):
        result = self.data
        for key, value in kwargs.items():
            result = list(filter(lambda x: value in x[key], result))
        return result if len(result) > 0 else list(People.msg["nodata"])
filters = {"FirstName": "", "LastName": "", "Job": ""}
print("Please enter filter data")
for key in filters.keys():
    print(key, ":", sep="")
    filters[key] = input()
people = People(data)
for x in people.get(filters):
    print(x)