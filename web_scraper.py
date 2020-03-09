{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "web_scraper.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP6tW3aeri1QvLBguDzpwoL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kvapiltomas/projects/blob/master/web_scraper.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qLWtbh8xT0II",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import os\n",
        "\n",
        "%matplotlib inline"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wFQ9WtFVUV2w",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "urls = ['https://www.idnes.cz/zpravy/zahranicni','https://www.idnes.cz/zpravy/domaci']\n",
        "\n",
        "def get_data(urls):\n",
        "  \n",
        "  for url in urls:\n",
        "    data = requests.get(url)\n",
        "    bs = BeautifulSoup(data.content, 'html.parser')\n",
        "    if data:\n",
        "      print('s')\n",
        "    else:\n",
        "      print('n')\n",
        "    print(bs)\n",
        "  headline = bs.find_all('div', class_ = 'h3')\n",
        "  article = bs.find_all('p', class_ = 'perex')\n",
        "  headlines = [h.get_text() for h in headline]\n",
        "  articles = [a.get_text() for a in article]\n",
        "  #news_data = pd.DataFrame({'headline': headlines,\n",
        "  #                         'arcticle': articles})\n",
        "  #news_data.extend(headlines,articles)\n",
        "  print(headline)\n",
        "  #print(article)\n",
        "  #news_data.extend(h)\n",
        "  #print(news_data) \n",
        "               \n",
        "  #strip_html_tags(articles)           \n",
        "  #news_data.extend(articles)\n",
        "  #news_data(articles)\n",
        "\n",
        "get_data(urls)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KypA84fhUFEC",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "urls = ['https://www.idnes.cz/zpravy/zahranicni','https://www.idnes.cz/zpravy/domaci']\n",
        "\n",
        "url = 'https://www.idnes.cz/zpravy/domaci'\n",
        "data = requests.get(url)\n",
        "bs = BeautifulSoup(data.content, 'html.parser')\n",
        "if data:\n",
        "  print('s')\n",
        "else:\n",
        "  print('n')\n",
        "#print(bs.prettify())\n",
        "#headline = bs.find('h3').string\n",
        "article = bs.find_find_all('p', class_ = 'perex').get_text()\n",
        "#print(articl)\n",
        "headline = bs.find_all('h3').get_text()\n",
        "#print(headline)\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
