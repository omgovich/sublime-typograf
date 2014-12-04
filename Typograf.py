import sublime, sublime_plugin, urllib

class TypografCommand(sublime_plugin.TextCommand):

	def run(self, edit, **args):
		url = 'http://www.typograf.ru/webservice/'
		xml = '<?xml version="1.0" encoding="windows-1251" ?><preferences><tags delete="0">' + args['tags'] + '</tags></preferences>'
		for region in self.view.sel():
			source =  sublime.get_clipboard() if args['paste'] else self.view.substr(region)
			if source:
				params = urllib.parse.urlencode({ 'text': source, 'chr': 'UTF-8', 'xml': xml })
				params = params.encode('windows-1251')
				response = urllib.request.urlopen(url, params)
				lines = response.read().decode("utf-8")
				self.view.replace(edit, region, lines)