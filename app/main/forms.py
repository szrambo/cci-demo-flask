from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
    TextAreaField, SelectField, HiddenField
from wtforms.validators import Required, Length, Email, ValidationError


def validate_tags(form, field):
    if field.data:
        for x in field.data.split(','):
            if len(x) not in range(200+1):
                raise ValidationError(
                    'All tags must be less than 200 characters')


class NoteForm(FlaskForm):
    title = StringField('Title:', validators=[Required(), Length(1, 200)])
    body = HiddenField()
    tags = StringField(validators=[validate_tags])
    notebook = SelectField(coerce=int)
    submit = SubmitField('Submit')


class ShareForm(FlaskForm):
    recipient_email = StringField(
        'Recipient Email', validators=[Required(), Length(1, 254), Email()])
    submit = SubmitField('Share')


class NotebookForm(FlaskForm):
    title = StringField('Title:', validators=[Required(), Length(1, 200)])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    search_field = StringField()
    submit = SubmitField('Search')
