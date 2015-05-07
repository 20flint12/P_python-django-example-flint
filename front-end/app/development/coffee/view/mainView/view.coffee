module.exports = do ->
	Backbone = require 'backbone'
	$		 = require 'jquery'
	mustache = require 'mustache'

	getTemplate = (baseTemplte) -> 

		(model) ->
			mustache.render baseTemplte, model 

	class View extends Backbone.View
		el: '.astro-calendar-list'
		template: getTemplate $('#astro-week-template').html()
		events: 
			'click .day-number': 'showFullInfo'
		initialize: ->
			do @bindEvents
			# do @collection.requestModels
		
		bindEvents: ->
			@listenTo @collection, 'reset', @render

		render: (collection) =>
			template = ''
			self	 = @

			collection.each (val) ->
				template += self.template val.toJSON()

			@$el.empty().append template

		showFullInfo: (e) ->
			day   = $ e.target
			id    = day.data 'day-id'
			model = @collection.get id
			
			model.set 'isShowing', true

	View