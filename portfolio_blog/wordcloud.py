"""Wordcloud image creation for portfolio_blog app"""

import os
import base64
import io
import urllib.parse
from typing import List, Optional, Union
from django.contrib.staticfiles import finders
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image
from wordcloud import STOPWORDS, WordCloud


def show_wordcloud(data: Optional[Union[List[str], str]]) -> Optional[Image.Image]:
    """Convert matplotlib data to image.

    Args:
        data (Optional[Union[List[str], str]]): List of words for wordcloud.

    Returns:
        Optional[Image.Image]: Wordcloud image or None if error occurs.
    """
    try:
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(
            background_color="white",
            max_words=200,
            max_font_size=40,
            repeat=True,
            scale=7,
            random_state=0,
            stopwords=stopwords,
        )
        wordcloud.generate(str(" ".join(data)))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        custom_font_path = finders.find("fonts/BBHSansBartle-Regular.ttf")
        custom_font = fm.FontProperties(fname=custom_font_path)
        plt.text(
            x=0.5,  # Horizontal position (0.5 = center)
            y=0.5,  # Vertical position (0.5 = center)
            s=os.getenv("DJANGO_WORDCLOUD", "DEVOPS"),  # The text to display
            ha="center",  # Horizontal alignment ('left', 'center', 'right')
            va="center",  # Vertical alignment ('top', 'center', 'bottom')
            size="xx-large",  # Font size
            fontproperties=custom_font,  # Custom font properties
            color="black",  # Text color
            weight="bold",  # Font weight
            backgroundcolor="white",  # Background color
            transform=plt.gca().transAxes,  # Specify coordinates are relative to the axes
        )
        image = io.BytesIO()
        plt.savefig(image, format="png")
        image.seek(0)
        string = base64.b64encode(image.read())
        image_64 = "data:image/png;base64," + urllib.parse.quote_plus(string)

        return image_64

    except ValueError:
        return None
