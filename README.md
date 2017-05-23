# webcomplete.vim

A Vim plugin that completes words from the currently open web page in your
browser.

![demo](./demo.gif)

# Todo
- it should only search for words that the user is currently typing
  or it should only downloads the words from the page once or if the user changed tab
- it is very slow
- we can probably remove the sh and move all python together (probably have a look at other completion engines)
- it seems to steal focus from vim and give it to firefox when typing in vim sometimes (check if can reproduce first)


# Requirements
- `pip install --user marionette_driver` (note this only works with pip2)
- start firefox using `firefox -marionette`

# Installation

With [vim-plug](https://github.com/junegunn/vim-plug):

```
Plug 'thalesmello/webcomplete.vim'
```

## Using with deoplete

[`deoplete`](https://github.com/Shougo/deoplete.nvim/) is an awesome asynchronous
completion engine for Neovim. `webcomplete` works with `deoplete` out of the box.
Just start typing to see suggestions of words comming from your browser.

## Using with `completefunc` or `omnifunc`

Vim allows you to define a `completefunc` or an `omnifunc` to give you
completions during insert mode. `webcomplete` provides you with a function that
you can plug into these built in features.

To set it up, use either of the two lines below:
```
" Use <C-X><C-U> in insert mode to get completions
set completefunc=webcomplete#complete

" Use <C-X><C-O> in insert mode to get completions
set omnifunc=webcomplete#complete
```

# Limitations

* Assumes you have only one browser window opened. If there is more than one
  window open, it picks just one of them.

# Contributing

If you would like to contribute to the project by supporting your browser or
operating system, I would be happy to accept pull requests.

# Inspiration

The project was only possible with the [help of Reddit user 18252](https://www.reddit.com/r/commandline/comments/4j73um/any_way_of_getting_the_text_of_open_chrome_pages/d34ftzx)
and by looking at [tmux-complete.vim](https://github.com/wellle/tmux-complete.vim) as reference when implementing this plugin.
