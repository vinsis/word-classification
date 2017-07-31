## word-classification

Accuracy: ~80%

### Overview
A piece of code that tells classifies any given word sounds as Japanese, English or Spanish based on its structure.

For example, it classifies:
* "*mirodo*" as Japanese
* "*mirado*" as Spanish
* "*mirror*" as English

It is able to detect subtle differences between words.
For example, it classifies "**Texas**" as English but "**Tejas**" as Spanish. **Texas** is actually anglicized form of the Spanish word **Tejas**. It also classifies Colorado as Spanish.

### How to use it
```
import classifier
classifier.trainData()
classifier.classifyWord('hello')
```
