# markdown-emdash

Extension for [python-markdown](https://python-markdown.github.io/) that replaces all triple dashes
(`---`) with em-dashes (`&mdash;`).

More information on [extensions here](https://python-markdown.github.io/extensions/).

## Installation

```
pip install markdown-emdash
```

## Usage

```python
markdown.markdown(some_text, extensions=[EmDashExtension()])
```
