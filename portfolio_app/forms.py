"""Django forms for the portfolio_app app."""

from django import forms


class SearchForm(forms.Form):
    """Form for searching blog posts."""

    search_query = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(attrs={"placeholder": "Search..."})
    )
