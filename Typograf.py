import sublime, sublime_plugin, urllib

class TypografCommand(sublime_plugin.TextCommand):  
	def run(self, edit):
		url = 'http://www.typograf.ru/webservice/'
		for region in self.view.sel():
			if not region.empty():
				selection = self.view.substr(region)
				params = urllib.parse.urlencode({ 'text': selection, 'chr': 'UTF-8' })
				params = params.encode('windows-1251')
				response = urllib.request.urlopen(url, params)
				lines = response.read().decode("utf-8");
				self.view.replace(edit, region, lines)