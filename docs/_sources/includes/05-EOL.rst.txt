
*****************
|EOL| ideas/plans
*****************

- Linux Mint 18.x/Ubuntu 16.04.x |EOL| is 2021.
- Remove all retro-compatible code from all xlets. They all are marked with the string *Mark for deletion on EOL*.
- Avoid at all cost to make xlets **multiversion**. I already went through that path. It wasn't pretty all the nonsense that I had to endure.
- Convert all JavaScript code into ECMAScript 2015 syntax. By 2021, I might get used to that annoyance. LOL

    + **Step 1 (Done):** Eradicate the use of the **Lang** Cjs module in favor of arrow/standard functions.
    + **Step 2 (Done):** Convert all functions (that can be converted) to arrow functions.

- Remove all ``try{}catch{}`` blocks on xlets ``_init`` methods. Newer versions of Cinnamon already uses these code blocks to wrap xlets initialization. Keep an eye on it in case that they decide to change this yet again.
- Don't bother to implement the use of ``setTimeout``, ``clearTimeout``, ``setInterval`` and ``clearInterval`` to replace the use of ``Mainloop.timeout_add`` and ``Mainloop.source_remove``. It was added around Cinnamon 4.0.x. Lets see if they get forced down CJS' throat before considering their usage.
- Reluctant to implement ``throttle`` method. Mainly because it uses ``setTimeout``, ``clearTimeout``. And with such a complex feature, I'm not willing to depend on it due to the always-changing-never-stable environment like Cinnamon. I prefer to keep using the *classic* ``Mainloop.timeout_add``-``Mainloop.source_remove`` combination to emulate the *throttle behavior*.


.. contextual-admonition::
    :title: Detailed list of changes

    - settings-schema.json file:

        + Change the use of the ``checkbox`` widget for ``switch``.
        + Implemennt the use of the ``layout`` key to create tabs for the setting windows of the xlets that need them. Ignore the xlets that use my own settings framework.

    - Cinnamon API changes:

        + Remove argument from ``SignalManager.SignalManager`` initialization.
