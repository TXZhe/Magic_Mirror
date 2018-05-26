hair_clothes=[  "fluffy hairstyle",
        "flat hairstyle",
        "flat head of hair",
        "short hair",
        "oblique bangs",
        "neat bangs",
        "both sides of face have hair",
        "black hair",
        "make the chin prominence or contraction",
        "Chinese style",
        "slightly thick shape on both sides of the head",

        "not match V-neckline",
        "not match round neck or narrow neck",
        "not match large lapel",
        "not match clothes with rough in texture, gray in color",
        "not match complex style",
        "level collar, such as arc collar, low collar and square collar",
        "double lapel, tie collar, and other small collar",
        "choose the collar style that can cover the neck.",
        "light or bright colors with some checks, horizontal stripes",
        "T-shirt with a pattern on the chest",
        "soft, comfortable and light colored clean clothes",
        "simple type of clothes and canvas shoes",
        "a slightly deeper square collar, sharp collar, low collar or switch collar"]

def look_up(hairstyle = [], clothesstyle = []):
    rec = "I recommend you "
    for i in hairstyle:
        rec = rec+hair_clothes[i-1]+". "
    rec = rec+'\n'
    for i in clothesstyle:
        rec = rec+hair_clothes[i-1]+". "
    rec = rec+'\n'
    return rec
