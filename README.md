os-autoinst/openQA needles for openSUSE
[![Build Status](https://travis-ci.org/os-autoinst/os-autoinst-needles-opensuse.svg?branch=master)](https://travis-ci.org/os-autoinst/os-autoinst-needles-opensuse)
=================================================================================================================================================================================================================================
os-autoinst-needles-opensuse is repo which contains needles for the tests which
are stored in [os-autoinst-distri-opensuse](https://github.com/os-autoinst/os-autoinst-distri-opensuse)
repository.

More information about needles and how they are used can be found in
[openQA Getting Started guide](https://github.com/os-autoinst/openQA/blob/master/docs/GettingStarted.asciidoc#needles).

## How to contribute

Fork the repository and make some changes.
Once you're done with your changes send a pull request. If you have test code
changes relevant to your PR, please include reference in the description.

You have to agree to the license. Thanks!
If you have questions, visit us on irc.libera.chat in #opensuse-factory or
ask on our mailing list opensuse-factory@opensuse.org.

### How to create needles

The easiest way to create or update needle is to use openQA needle editor.
Simply navigate to the screen where you need to create a needle and press button
with pin icon. Define required tags, areas to match and press save button.
After that png an json files will be created in the needles directory used in
the setup (`/var/lib/openqa/tests/opensuse/products/opensuse/needles` by default).

When developing new test, interactive mode is handy too to create multiple
needles during single run. Please, refer to [openQA documentation](https://github.com/os-autoinst/openQA/blob/master/docs/GettingStarted.asciidoc#interactive-mode).

### Best practices

Some say that creating good needle is an art. And it is challenging sometimes.
Here are some tips:
* Use self-explanatory names for the tags.
* Use workaround flag with bug reference in the file name. For the scenarios
when one needs a needle just to make test progress further, but don't accept
current behavior "workaround" property can be used. It will mark failing
test module as soft-failed and bug reference can be used to identify the
reason why test behavior is not accepted.
* Cover areas which assert that page is fully loaded. Sometimes content can
still be missing on the screen which is verified and can interfere with next
steps execution.
* Create multiple small areas or increase match level if asserting font or
text. When big area is selected, small changes like font may not cause mismatch
and will be accepted with default match level of 96%.
