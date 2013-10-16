import sublime, sublime_plugin  

class TypografCommand(sublime_plugin.TextCommand):  
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				# Get the selected text
				s = self.view.substr(region)
				# Replace text
				s = s.replace(' ', '')
				# Replace the selection with transformed text
				self.view.replace(edit, region, s)