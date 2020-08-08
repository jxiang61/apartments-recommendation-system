var express = require('express');
var app = express();
var parser = require('body-parser');
var mongoose = require('mongoose');
var passport = require('passport');
var localStrategy = require('passport-local');
var User = require('./models/user.js');
var flash = require('connect-flash');

var indexRoutes = require('./routes/index.js'),
	attractionRoutes = require('./routes/attractions.js');

var methodOverride = require('method-override');

// seedDB();
// fix the  warning from mongoose
mongoose.set('useUnifiedTopology', true);
mongoose.connect("mongodb+srv://attractionYelp:jiaoyi1994@attractionyelpcluster-hzqiw.mongodb.net/test?retryWrites=true&w=majority", {
	useNewUrlParser: true,
	useCreateIndex: true
});
//mongoose.connect("mongodb://localhost/yelp", {useNewUrlParser: true});

//
app.use(parser.urlencoded({extended: true}));
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));
app.use(methodOverride('_method'));
app.use(flash());
// passport config
app.use(require('express-session')({
	secret: 'attraction yelp like',
	resave: false,
	saveUnitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
passport.use(new localStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

// make currentUser accessible
app.use(function(req, res, next) {
	res.locals.currentUser = req.user;
	res.locals.error = req.flash('error');
	res.locals.success = req.flash('success');
	next();
});

app.use(indexRoutes);
app.use(attractionRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, function() {
	console.log('server start');
})