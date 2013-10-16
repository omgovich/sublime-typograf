import sublime, sublime_plugin, urllib

class TypografCommand(sublime_plugin.TextCommand):  
	def run(self, edit):
		url = 'http://www.typograf.ru/webservice/'
		for region in self.view.sel():
			if not region.empty():
				selection = self.view.substr(region)
				params = urllib.parse.urlencode({ 'text':selection })
				params = params.encode('windows-1251')
				response = urllib.request.urlopen(url, params)
				self.view.replace(edit, region, str(response.read()))