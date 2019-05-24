# Articles

Create an application that can display the articles and who has seen it.

- You shall not change the given data structures.
- The template can only receive a list.
- You must create the template based on the provided HTML
  - Use variables, for loops, if conditions and filters
  - The content must be truncated at 225 characters

## Python boilerplate

```python
articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]

@app.route("/articles")
def list_articles():
    return render_template("articles.html", articles=articles)
```

## The rendered template

```html
<p>
  Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per
  ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot
  qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im red...
</p>
<p>Seen by John, Jane, and Bob</p>
<p>
  Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam
  tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim
  ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ...
</p>
<p>Seen by John, and Jane</p>
<p>
  Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus
  differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae
  perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam id...
</p>
<p>Seen by John</p>
<p>
  Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei
  inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.
</p>
<p>No one has seen this article before.</p>
```