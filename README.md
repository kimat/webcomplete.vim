[deoplete.nvim](https://github.com/Shougo/deoplete.nvim) source to autocomplete words from the current [Firefox](https://www.mozilla.org/en-US/firefox/new/) tab.

## Requirements

- [deoplete.nvim](https://github.com/Shougo/deoplete.nvim)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- marionette_driver
- firefox

## Installation

```vim
Plug 'kimat/webcomplete.vim'
```

## Usage

```sh
firefox -marionette
```


## Notes

- we could also do line completions similary to [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming)
- we could also do line completions but only on `<code>` or `<pre>` parts of the webpage
- this could become a languageServer

## Credits

- [shougo](https://github.com/shougo)
- [thalesmello](https://github.com/thalesmello)
