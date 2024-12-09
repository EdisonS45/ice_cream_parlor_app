from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired

# Form for adding/updating seasonal flavor
class FlavorForm(FlaskForm):
    flavor_name = StringField('Flavor Name', validators=[DataRequired()])
    season = StringField('Season', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    description = TextAreaField('Description')

# Form for adding/updating ingredient
class IngredientForm(FlaskForm):
    ingredient_name = StringField('Ingredient Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])

# Form for flavor suggestion
class SuggestionForm(FlaskForm):
    flavor_name = StringField('Flavor Name', validators=[DataRequired()])
    description = TextAreaField('Description')

# Form for allergy concern
class AllergyForm(FlaskForm):
    allergen_name = StringField('Allergen Name', validators=[DataRequired()])
    customer_message = TextAreaField('Message')