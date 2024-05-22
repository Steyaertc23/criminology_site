from django import forms

MISDOMEANOR_CLASSES = [
    (-1, 'Misdomeanor Class...'),
    (1, 'Class 1'),
    (2, 'Class 2'),
    (3, 'Class 3'),
    (4, 'Class 4')
]

FELONY_CLASSES = [
    (-1, 'Felony Class...'),
    (1, 'Class 1'),
    (2, 'Class 2'),
    (3, 'Class 3'),
    (4, 'Class 4'),
    (5, 'Class 5'),
    (6, 'Class 6'),
    (6, 'Class 6'),
]

class AddFelon(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name of felon', 'class':'form'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name of felon', 'class':'form'}))
    class_ = forms.ChoiceField(widget=forms.Select(attrs={'class':'choose'}, choices=FELONY_CLASSES))

class AddMisdomeanor(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name of person who committed misdomeanor', 'class':'form'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name of person who committed misdomeanor', 'class':'form'}))
    class_ = forms.ChoiceField(widget=forms.Select(attrs={'class':'choose'}, choices=MISDOMEANOR_CLASSES))