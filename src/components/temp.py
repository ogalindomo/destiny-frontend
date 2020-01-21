import sys, json

def load_vector(string_vector):
    return json.loads(string_vector)

def create_metadata(vector):
    image_id = str(vector.pop('imageID'))
    document = open("Gallery/"+image_id+'.txt', "w")
    document.write(str(vector))
    document.close()

if __name__ == "__main__":
    vector = load_vector(sys.argv[1])
    create_metadata(vector)
