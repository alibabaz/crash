import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45,
					show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'system-design-primer',
						'public-apis']

plot_dicts = [
	{'value': 70186, 'label': "Description of awesome-python"},
	{'value': 69422, 'label': "Description of system-design-primer"},
	{'value': 59228, 'label': "Description of public-apis"}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')