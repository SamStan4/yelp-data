import json

business_json_fname = "yelp_business.JSON"
business_txt_fname = "yelp_business.txt"
checkin_json_fname = "yelp_checkin.JSON"
checkin_txt_fname = "yelp_checkin.txt"
review_json_fname = "yelp_review.JSON"
review_txt_fname = "yelp_review.txt"
user_json_fname = "yelp_user.JSON"
user_txt_fname = "yelp_user.txt"

class colors:
    F_BLACK = '\033[30m'
    F_RED = '\033[31m'
    F_GREEN = '\033[32m'
    F_YELLOW = '\033[33m'
    F_BLUE = '\033[34m'
    F_MAGENTA = '\033[35m'
    F_CYAN = '\033[36m'
    F_WHITE = '\033[37m'
    B_BLACK = '\033[40m'
    B_RED = '\033[41m'
    B_GREEN = '\033[42m'
    B_YELLOW = '\033[43m'
    B_BLUE = '\033[44m'
    B_MAGENTA = '\033[45m'
    B_CYAN = '\033[46m'
    B_WHITE = '\033[47m'
    RESET = '\033[0m'
    
def clean_string(s : str) -> str:
    return s.replace("'","''").replace('\n', " ").replace("\r", "")

def get_attributes(attributes : dict) -> list:
    L = []
    for (attribute, value) in list(attributes.items()):
        if isinstance(value, dict):
            L += get_attributes(value)
        else:
            L.append((attribute,value))
    return L

def parse_yelp_business_file() -> None:
    try:
        input_stream = open(business_json_fname, "r")
    except:
        print(" {}error: {} not found in current directory{} ".format(colors.B_RED, business_json_fname, colors.RESET), end='')
        return
    output_stream = open(business_txt_fname, "w")
    for input_line in input_stream:
        json_data = json.loads(input_line)
        buisness_ID = json_data["business_id"]
        output_stream.write("'{}','{}','{}','{}','{}',{},{},{},{},{}\n".format(\
            clean_string(json_data["name"]),\
            clean_string(json_data["address"]),\
            clean_string(json_data["city"]),\
            json_data["state"],\
            json_data["postal_code"],\
            str(json_data["latitude"]),\
            str(json_data["longitude"]),\
            str(json_data["stars"]),\
            str(json_data["review_count"]),\
            str(json_data["is_open"])))
        for i in json_data["categories"]:
            output_stream.write("'{}','{}'\n".format(buisness_ID, i))
        for (i, j) in json_data["hours"].items():
            output_stream.write("'{}','{}','{}','{}'\n".format(buisness_ID, str(i), str(j.split('-')[0]), str(j.split('-')[1])))
        for (i, j) in get_attributes(json_data["attributes"]):
            output_stream.write("'{}','{}','{}'\n".format(buisness_ID, str(i), str(j)))    
    output_stream.close()
    input_stream.close()
    
def parse_yelp_review_file() -> None:
    try:
        input_stream = open(review_json_fname, "r")
    except:
        print(" {}error: {} not found in current directory{} ".format(colors.B_RED, review_json_fname, colors.RESET), end='')
        return
    output_stream = open(review_txt_fname, "w")
    for input_line in input_stream:
        json_data = json.loads(input_line)
        output_stream.write("'{}','{}','{}',{},'{}','{}',{},{},{}\n".format(\
            json_data["review_id"],\
            json_data["user_id"],\
            json_data["business_id"],\
            str(json_data["stars"]),\
            json_data["date"],\
            clean_string(json_data["text"]),\
            str(json_data["useful"]),\
            str(json_data["funny"]),\
            str(json_data["cool"])))
    output_stream.close()
    input_stream.close()
    
def parse_yelp_user_data_file() -> None: 
    try:
        input_stream = open(user_json_fname, "r")
    except:
        print(" {}error: {} not found in current directory{} ".format(colors.B_RED, user_json_fname, colors.RESET), end='')
        return
    output_stream = open(user_txt_fname, "w")
    for input_line in input_stream:
        json_data = json.loads(input_line)
        user_ID = json_data["user_id"]
        output_stream.write("'{}','{}','{}',{},{},{},{},{},{}\n".format(\
            user_ID,\
            clean_string(json_data["name"]),\
            clean_string(json_data["yelping_since"]),\
            str(json_data["review_count"]),\
            str(json_data["fans"]),\
            str(json_data["average_stars"]),\
            str(json_data["funny"]),\
            str(json_data["useful"]),\
            str(json_data["cool"]),))
        for i in json_data["friends"]:
            output_stream.write("'{}','{}'\n".format(user_ID, i))
    output_stream.close()
    input_stream.close()
    
def parse_yelp_check_in_file() -> None:
    try:
        input_stream = open(checkin_json_fname, "r")
    except:
        print(" {}error: {} not found in current directory{} ".format(colors.B_RED, checkin_json_fname, colors.RESET), end='')
        return
    output_stream = open(checkin_txt_fname, "w")
    for input_line in input_stream:
        json_data = json.loads(input_line)
        business_ID = json_data["business_id"]
        for (i, j) in json_data["time"].items():
            for (k, l) in j.items():
                output_stream.write("'{}','{}','{}',{}\n".format(business_ID, i, k, str(l)))
    output_stream.close()
    input_stream.close()

def parse_everything() -> None:
    print("{}parsing {} into {}...{}".format(colors.F_CYAN, business_json_fname, business_txt_fname, colors.RESET))
    parse_yelp_business_file()
    print("{}[{}DONE{}]{}".format(colors.F_MAGENTA, colors.F_GREEN, colors.F_MAGENTA, colors.RESET))
    print("{}parsing {} into {}...  {}".format(colors.F_CYAN, checkin_json_fname, checkin_txt_fname, colors.RESET))
    parse_yelp_check_in_file()
    print("{}[{}DONE{}]{}".format(colors.F_MAGENTA, colors.F_GREEN, colors.F_MAGENTA, colors.RESET))
    print("{}parsing {} into {}...{}    ".format(colors.F_CYAN, review_json_fname, review_txt_fname, colors.RESET))
    parse_yelp_review_file()
    print("{}[{}DONE{}]{}".format(colors.F_MAGENTA, colors.F_GREEN, colors.F_MAGENTA, colors.RESET))
    print("{}parsing {} into {}...{}        ".format(colors.F_CYAN, user_json_fname, user_txt_fname, colors.RESET))
    parse_yelp_user_data_file()
    print("{}[{}DONE{}]{}".format(colors.F_MAGENTA, colors.F_GREEN, colors.F_MAGENTA, colors.RESET))

parse_everything()

# input_stream = open(review_json_fname, "r")
# for line in input_stream:
#     data = json.loads(line)
#     if data["review_id"] == "SJ5eW--P7YKgAxrQV268rg":
#         print(data)
# input_stream.close()