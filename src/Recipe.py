## require requests, BeautifulSoup, re, json
class Recipe:

################################################################################################ init empty recipe
    def __init__(self):

        self.title = ''
        self.url = ''
        self.imgurl = ''
        self.desc = ''

        self.ingredients = []
        self.steps = []
        self.tags = []
        self.nutritions = {}
        self.serving = 0

        self.yiel = ''
        self.activetime = ''
        self.totaltime = ''

        self.rating = 0
        self.reviewcount = 0
        self.makeagain = 0
        self.reviews = []


############################################################################ init recipe using a recipe detial page
    def __init__(self, url):

        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')

        self.title = self.build_title(soup)
        self.url = url
        self.imgurl = self.build_imgurl(soup)
        self.desc = self.build_desc(soup)

        self.ingredients = self.build_ingredients(soup)
        self.steps = self.build_steps(soup)
        self.tags = self.build_tags(soup)
        self.nutritions = self.build_nutritions(soup)
        self.serving = self.build_serving(soup)

        self.yiel = self.build_yield(soup)
        self.activetime = self.build_activetime(soup)
        self.totaltime = self.build_totaltime(soup)

        self.rating = self.build_rating(soup)
        self.reviewcount = self.build_reviewcount(soup)
        self.makeagain = self.build_makeagain(soup)
        self.reviews = self.build_reviews(soup)


########################################################################### fuctions: get infomation from a page
    def build_title(self, soup):
        try:
            el = soup.select('div.main-content div.title-source h1')
            title = re.search(r'\">(.+)<', str(el)).group(1).strip()
            return title
        except:
            print("Title Wrong: "+self.url)
            return ''

    def build_imgurl(self, soup):
        try:
            el = soup.select('div.main-content img["srcset"]')
            imgurl = re.search(r'srcset="(.+)"\/>', str(el)).group(1)
            return imgurl
        except:
            print("IMG Wrong: "+self.url)
            return ''

    def build_desc(self, soup):
        try:
            el = soup.select('div.main-content div.dek')
            desc = re.search(r'<p>(.+)<\/p>', str(el)).group(1).strip()
            return desc
        except:
            #print("Desc Wrong: "+self.url)
            return ''


    def build_ingredients(self, soup):
        try:
            ingredients = []
            els = soup.select('div.main-content div.ingredients-info li.ingredient')
            for el in els:
                ingredients.append(re.search(r'<li.+>(\s*.+\s*)<\/li>', str(el)).group(1).strip())
            return ingredients
        except:
            print("Ingredients Wrong: "+self.url)
            return []

    def build_steps(self, soup):
        try:
            steps = []
            els = soup.select('div.main-content div.instructions li.preparation-step')
            for el in els:
                steps.append(re.search(r'<li.+>(\s*.+\s*)<\/li>', str(el)).group(1).strip())
            return steps
        except:
            print("Steps Wrong: "+self.url)
            return []

    def build_tags(self, soup):
        try:
            tags = []
            els = soup.select('div.main-content dl.tags a')
            for el in els:
                tags.append(re.search(r'\".+>(.+)<\/dt>', str(el)).group(1))
            return tags
        except:
            print("Tags Wrong: "+self.url)
            return []

    def build_nutritions(self, soup):
        try:
            nutritions = {}
            labels = soup.select('div.main-content span.nutri-label')
            values = soup.select('div.main-content span.nutri-data')
            for i in range(len(labels)):
                n = re.search(r'\">(.+)<\/', str(labels[i])).group(1)
                v = re.search(r'\">(.+)<\/', str(values[i])).group(1)
                v = float(v.split(' ')[0])
                nutritions[n] = v
            return nutritions
        except:
            #print("Nutritions Wrong: "+self.url)
            return {}

    def build_serving(self, soup):
        try:
            el = soup.select('div.main-content span.per-serving')
            serving = re.search(r'.+(\d+).+',str(el)).group(1)
            return float(serving)
        except:
            #print("Serving Wrong: "+self.url)
            return 0


    def build_yield(self, soup):
        try:
            el = soup.select('div.main-content dd.yield')
            y = re.search(r'\">(.+)<', str(el)).group(1)
            return y
        except:
            #print("Yield Wrong: "+self.url)
            return ''

    def build_activetime(self, soup):
        try:
            el = soup.select('div.main-content dd.active-time')
            active = re.search(r'\">(.+)<', str(el)).group(1)
            return active
        except:
            #print("Activetime Wrong: "+self.url)
            return ''

    def build_totaltime(self, soup):
        try:
            el = soup.select('div.main-content dd.total-time')
            total = re.search(r'\">(.+)<', str(el)).group(1)
            return total
        except:
            #print("Totaltime Wrong: "+self.url)
            return ''


    def build_rating(self, soup):
        try:
            el = soup.select('div.main-content span.rating')
            rating = re.search(r'\">(.+)\/\d', str(el)).group(1)
            return float(rating)
        except:
            print("Rating Wrong: "+self.url)
            return 0

    def build_reviewcount(self, soup):
        try:
            el = soup.select('div.main-content span.reviews-count')
            reviewcount = re.search(r'(\d+)', str(el)).group(1)
            return float(reviewcount)
        except:
            print("Reviewcount Wrong: "+self.url)
            return 0

    def build_makeagain(self, soup):
        try:
            el = soup.select('div.main-content div.prepare-again-rating span')
            makeagain = re.search(r'(\d+)', str(el)).group(1)
            return float(makeagain)
        except:
            print("MakeagainRating Wrong: "+self.url)
            return 0

    def build_reviews(self, soup):
        try:
            reviews = []
            els = soup.select('div.main-content div.reviews li div.review-text p')
            for el in els:
                review = re.search(r'\">(.+[\s\S]*)<', str(r)).group(1).strip()
                reviews.append(review)
            return reviews
        except:
            #print("Reviews Wrong: "+self.url)
            return []


######################################################################################################### to string
    def __str__(self):
        string = "\nTitle: " + self.title + "\nURL: " + self.url + "\nIMG URL: " + self.imgurl + "\nDesc: " + self.desc + "\nIngredients: " + str(self.ingredients) + "\nSteps: " + str(self.steps) + "\nTags: " + str(self.tags) + "\nNutritions: " + str(self.nutritions) + "\nServing: " + str(self.serving) + "\nYield: " + self.yiel + "\nActive time: " + self.activetime + "\nTotal time: " + self.totaltime + "\nRating: " + str(self.rating) + "\nReview count: " + str(self.reviewcount) + "\nMake again: " + str(self.makeagain) + "\nReviews: " + str(self.reviews)
        return string

######################################################################################################### getters
    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_imgurl(self):
        return self.imgurl

    def get_desc(self):
        return self.desc


    def get_ingredients(self):
        return self.ingredients

    def get_steps(self):
        return self.steps

    def get_tags(self):
        return self.tags

    def get_nutritions(self):
        return self.nutritions

    def get_serving(self):
        return self.serving


    def get_yield(self):
        return self.yiel

    def get_activetime(self):
        return self.activetime

    def get_totaltime(self):
        return self.totaltime


    def get_rating(self):
        return self.rating

    def get_reviewcount(self):
        return self.reviewcount

    def get_makeagain(self):
        return self.makeagain

    def get_reviews(self):
        return self.reviews
