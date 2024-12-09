from app import db

# Seasonal flavor offerings
class SeasonalFlavor(db.Model):
    flavor_id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Integer, default=1)
    description = db.Column(db.Text, nullable=True)

# Ingredient inventory
class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Flavor suggestions from customers
class FlavorSuggestion(db.Model):
    suggestion_id = db.Column(db.Integer, primary_key=True)
    flavor_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Allergy concerns
class AllergyConcern(db.Model):
    concern_id = db.Column(db.Integer, primary_key=True)
    allergen_name = db.Column(db.String(100), nullable=False)
    customer_message = db.Column(db.Text, nullable=True)

# Cart management for customers
class CartItem(db.Model):
    cart_item_id = db.Column(db.Integer, primary_key=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('seasonal_flavor.flavor_id'))
    quantity = db.Column(db.Integer, nullable=False)

    flavor = db.relationship('SeasonalFlavor', backref='cart_items')
