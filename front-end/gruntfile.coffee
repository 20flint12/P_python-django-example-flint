module.exports = (grunt) ->
	taskRunner = require 'load-grunt-tasks'
	devTasks   = [
		'haml:dev'
		'sass:dev' 
		'shell:coffeeCompile'
		'browserify:dev'
		'uglify:dev'
		'watch:dev'
	]
	testTasks = [
		'haml:dev'
		'sass:dev'
		'shell:coffeeCompile'
		'browserify:test'
		'watch:test'
	]
	config = 
		pkg: grunt.file.readJSON './package.json'
		developmentDir: './app/development'
		productionDir  : './app/production'
		watchFiles : [
			'<%=developmentDir%>/sass/body.scss',
			'index.html.haml',
			'<%=developmentDir%>/coffee/**'
		]
		haml: 
			dev:
				src: './index.html.haml'
				dest: './index.html'
		sass: 
			dev: 
				src: '<%=developmentDir%>/sass/body.scss'
				dest: '<%=productionDir%>/css/all.css'
		browserify: 
			dev:
				src: '<%=developmentDir%>/js/main.js'
				dest: '<%=productionDir%>/js/main.js'
			test: 
				src: '<%=developmentDir%>/js/main.js'
				dest: '<%=productionDir%>/js/main.min.js'
		shell: 
			coffeeCompile:
				command: 'coffee -b -c -o ./app/development/js ./app/development/coffee/'
		uglify:
			dev: 
				src: './app/production/js/main.js'
				dest: './app/production/js/main.min.js'
		watch: 
			dev:
				files: '<%=watchFiles%>'
				tasks: devTasks.splice 0, devTasks.length - 1
			test: 
				files: '<%=watchFiles%>'
				tasks: testTasks.slice 0, testTasks.length - 1

	grunt.initConfig config
	taskRunner grunt

	grunt.registerTask 'default', devTasks
	grunt.registerTask 'test', testTasks