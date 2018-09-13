[deoplete.nvim](https://github.com/Shougo/deoplete.nvim) source to autocomplete words from the current [Firefox](https://www.mozilla.org/en-US/firefox/new/) tab.

![gif](https://raw.githubusercontent.com/kimat/images/master/ff-complete.gif)

## Requirements

- [deoplete.nvim](https://github.com/Shougo/deoplete.nvim)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [marionette_driver](https://pypi.org/project/marionette_driver/)
- firefox

## Sample Installation

```sh
# install python modules
pip2 install --user beautifulsoup4 marionette_driver
```

```vim
" in ~/.vimrc
Plug 'kimat/webcomplete.vim'
```

## Usage

```sh
firefox -marionette
```


## Notes

- webcomplete shouldn't be called again if url didn't change
- we could also do line completions similary to [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming)
- we could also do line completions but only on `<code>` or `<pre>` parts of the webpage
- this could become a languageServer

## Credits

- [shougo](https://github.com/shougo)
- [thalesmello](https://github.com/thalesmello)
