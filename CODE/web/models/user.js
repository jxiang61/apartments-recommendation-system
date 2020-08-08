var mongoose = require('mongoose');
var userSchema = new mongoose.Schema({
	username: String,
	password: String
});

var passportLocalMongoose = require('passport-local-mongoose');

userSchema.plugin(passportLocalMongoose);

module.exports = mongoose.model('User', userSchema);