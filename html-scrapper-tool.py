from core.scrape import *
from profiles.autoimport import *

# a helper function to split and rejoin text based on name
def split_extra(name, txt):
    if name in ["Name", "Bio"]:
        return " ".join(txt.split())
    return txt

# a dictionary to map tag names to their respective functions
TAG_FUNCTIONS = {
    "span": span,
    "a": ahead,
    "div": div,
    "h1": h1,
    "p": phead,
    "section": section
}

def scrapefunc(_scrape, url, name, source):
    scraped = ""
    for sc in range(len(_scrape)):
        scrape_cname = _scrape[f"{sc}"]["cname"]
        scrape_name = _scrape[f"{sc}"]["name"]
        
        # to check if the cname exists in our mapping
        if scrape_cname in TAG_FUNCTIONS:
            scrape_function = TAG_FUNCTIONS[scrape_cname]
            scrape_text = scrape_function(source, _scrape[f"{sc}"]["class"])
            
            if scrape_text is not None:
                scrape_text = split_extra(scrape_name, scrape_text)
                parse(scrape_name, scrape_text, name, url)
                
                # reusable format for scraped data output
                scraped += (f"""[{color.green}{color.underline}{name}{color.reset}] 
                                {color.bold}{color.blue}{scrape_name}{color.reset} : 
                                {color.green}{color.underline}{scrape_text}{color.reset}\n""")
                
    return scraped
