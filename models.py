# models.py - Added to User model
class User(UserMixin, db.Model):
    # ... existing fields ...
    referral_code = db.Column(db.String(10), unique=True)
    referred_by = db.Column(db.String(10))
    referral_count = db.Column(db.Integer, default=0)

# routes.py - New routes
@app.route('/ref/<code>')
def referral(code):
    if current_user.is_authenticated:
        flash('You already have an account')
        return redirect(url_for('dashboard'))
    session['referral_code'] = code
    return redirect(url_for('register'))

@app.route('/referral-dashboard')
@login_required
def referral_dashboard():
    referrals = User.query.filter_by(referred_by=current_user.referral_code).all()
    return render_template('referral.html', referrals=referrals)
