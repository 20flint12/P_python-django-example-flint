module.exports = do ->
	$		   = require 'jquery'
	Backbone   = require 'backbone'

	Backbone.$ = $

	Model 	   = require './model/model.js'
	Collection = require './collection/collection.js'
	View 	   = require './view/view.js'
	

	$ ->
		# testCollect = generateTestCollection()

		model       = new Model
		collection  = new Collection
		view 	    = new View 'collection': collection
		console.log 'reseted'
		# collection.reset testCollect
		window.app = view

	# generateTestCollection = () ->
	# 	daysArr       = []
	# 	dayCount      = 0
	# 	previousMonth = Math.ceil (Math.random() * 6) 		

	# 	for val in [0...previousMonth]
	# 		daysArr.push 
	# 			dayNumber: dayCount++
	# 			isCurrentDay: false

	# 	currMonthDays = 35 - previousMonth
	# 	currentDay 	  = Math.ceil (Math.random() * currMonthDays)
		
	# 	for val in [previousMonth..currMonthDays]
	# 		day = 
	# 			dayNumber: dayCount++
	# 			isCurrentDay: false

	# 		day.isCurrentDay = true if currentDay is dayCount

	# 		daysArr.push day
