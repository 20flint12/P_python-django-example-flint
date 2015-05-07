module.exports =  do ->
	$		 = require 'jquery'
	Backbone = require 'backbone'
	Model 	 = require './../model/model.js'

	class Collection extends Backbone.Collection
		model: Model
		url: 'http://testastroflint2.cloudcontrolled.com/json/'
		initialize: ->
			do @bindEvents

		bindEvents: ->
			

		getReqData: ->
			timeWaiting = 5000

			url: @url
			data: {}
			dataType: 'json'
			timeout: timeWaiting
			cache: false
			success: @reqSuccess
			error: @reqError

		requestModels: ->
			data = do @getReqData

			@fetch data, reset: true
				
		reqSuccess: (response) =>
			console.log response
		reqError: =>
			console.log 'Sorry there is sime error while requesting'


	Collection