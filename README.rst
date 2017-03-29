.. .. image:: https://travis-ci.org/*github_repository*.svg?branch=master
    :target: https://travis-ci.org/*github_repository*

.. .. image:: https://coveralls.io/repos/github/*github_repository*/badge.svg?branch=master
    :target: https://coveralls.io/github/*github_repository*?branch=master


Pytuga-core implements the core features of Pytuguês language without a
dependency on the Pytuga Qt application. This might be useful for GUI-less
environments such as an online judge or if you just don't want/need a GUI
interface.

Most users will prefer to install the **pytuga** package that includes the
nice LOGO-based graphical interface. Pytuguês is a `Transpyled <http://github.com/transpyler/transpyler>`_
enabled language that translates Python to portuguese:

.. code-block:: pytuga

    função espiral(n):
        """
        Desenha uma espiral de n lados.
        """

        para cada x de 1 até n:
            frente(x * 20)
            esquerda(120)

    espiral(20)


Pytuga-core installs a IPython based shell that can be run with the command::

    $ python -m pytugacore

Boa programação!