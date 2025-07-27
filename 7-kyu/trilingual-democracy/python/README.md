## Trilingual democracy

Switzerland has [four official languages](https://www.fedlex.admin.ch/eli/cc/2009/821/en#art_5): German, French, Italian, and Romansh.<sup>1</sup>

When native speakers of one or more of these languages meet, they follow certain [regulations](https://www.fedlex.admin.ch/eli/cc/2010/355/en) to choose a language for the group.<sup>2</sup> Here are the rules for groups of exactly three<sup>3</sup> people:<sup>4</sup>

* When all three are native speakers of the same language, it also becomes their group's language.<sup>5a</sup>

* When two are native speakers of the same language, but the third person speaks a different language, all three will converse in the minority language.<sup>5b</sup>

* When native speakers of three different languages meet, they eschew these three languages and instead use the remaining of the four official languages.<sup>5c</sup>

The languages are encoded by the letters `D` for *Deutsch*, `F` for *Français*, `I` for *Italiano*, and `K` for *Rumantsch*.<sup>6</sup>

Your task is to write a function that takes a list of three languages and returns the language the group should use.<sup>7 8</sup>

Examples:<sup>9</sup>

* The language for a group of three native French speakers is French: `FFF` &rarr; `F`

* A group of two native Italian speakers and a Romansh speaker converses in Romansh: `IIK` &rarr; `K`

* When three people meet whose native languages are German, French, and Romansh, the group language is Italian: `DFK` &rarr; `I`

---

<sup>1</sup> The first sentence of the description and the first sentence of this footnote are true. Almost all other sentences in the description and the footnotes are complete hogwash.

<sup>2</sup> This footnote has no useful content. It was inserted solely to make the next footnote &ndash;&nbsp;at least in some sense&nbsp;&ndash; [self-referential](https://en.wikipedia.org/wiki/Self-reference).

<sup>3</sup> Thou shalt count to three, no more, no less. Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. Five is right out.

<sup>4</sup> These rules were carefully designed with a focus on practices that could be perceived as exclusive or discriminatory.

<sup>5a</sup> The first rule is based on pragmatics and aesthetics: choosing a language other than the one spoken by all three would introduce gratuitous friction and asymmetry.

<sup>5b</sup> The second rule is inspired by a strong sense of politeness and modesty: it would feel arrogant for the majority to impose its language upon the minority.

<sup>5c</sup> The third rule originates from a deep belief in fairness: picking one of the languages spoken in the group would arbitrarily privilege one member and disadvantage the two others.

<sup>6</sup> The choice of the letter `K` for *Rumantsch* was an accident &ndash; during the linguistic rule standardization process in 1964 a typist at the *Bundesamt für Organisation* misread a hand-written `R` as `K`. Unfortunately, correcting this mistake would break backwards compatibility.

<sup>7</sup> The input argument of your function will always be a string (or an array, depending on programming language) of exactly three upper-case characters from the set `D`, `F`, `I` and `K`, and the return value of your function must be a single upper-case character from this set.

<sup>8</sup> This footnote is a deceptive [non sequitur](https://en.wikipedia.org/wiki/Non_sequitur_(literary_device)), as it erroneously claims that the multilingual people of Switzerland are united by a shared fondness for [watchmaking](https://en.wikipedia.org/wiki/Watchmaking), [bit twiddling](https://en.wikipedia.org/wiki/Bit_twiddling), the [*Basic Latin*](https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)) Unicode block, and [Gruyère cheese](https://en.wikipedia.org/wiki/Gruyère_cheese).

<sup>9</sup> This is footnote 9, and it's just as nonsensical as footnotes 2, 3, and 8, since it merely observes that 9 happens to be the [bitwise exclusive-or](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of 2, 3, and 8.
