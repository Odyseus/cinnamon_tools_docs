
*****************
|EOL| ideas/plans
*****************

Done
====

- Remove all retro-compatible code from all xlets. They all are marked with the string *Mark for deletion on EOL*.
- Convert all JavaScript code into ECMAScript 2015 syntax. By 2021, I might get used to that annoyance. LOL

    + **Step 1:** Eradicate the use of the **Lang** Cjs module in favor of arrow/standard functions.
    + **Step 2:** Convert all functions (that can be converted) to arrow functions.
    + **Step 3:** Implement JavaScript classes.

- Remove all ``try{}catch{}`` blocks on xlets ``_init`` methods. Newer versions of Cinnamon already uses these code blocks to wrap xlets initialization. Keep an eye on it in case that they decide to change this yet again.


.. contextual-admonition::
    :title: Detailed list of changes

    - settings-schema.json file:

        + **Done** Change the use of the ``checkbox`` widget for ``switch``.
        + **Done** Implemennt the use of the ``layout`` key to create tabs for the setting windows of the xlets that need them. Ignore the xlets that use my own settings framework.

    - Cinnamon API changes:

        + **Done** Remove argument from ``SignalManager.SignalManager`` initialization.
