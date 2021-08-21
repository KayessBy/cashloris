from distutils.core import setup

setup(
    name="Cashloris",
    py_modules=["cashloris"],
    entry_points={"console_scripts": ["cashloris=cashloris:main"]},
    version="0.2.3",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="Kayess",
    author_email="ridvanm255@gmail.com",
    url="https://github.com/KayessBy/cashloris",
    keywords=["dos", "http", "cashloris"],
    license="MIT",
)
