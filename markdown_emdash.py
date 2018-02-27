from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown import util


class EmDashPattern(Pattern):
    """
    Replaces '---' with '&emdash;'.
    """
    def __init__(self):
        super(EmDashPattern, self).__init__('---')

    def handleMatch(self, m):
        # have to use special AMP_SUBSTITUTE character or it gets escaped
        return '{}mdash;'.format(util.AMP_SUBSTITUTE)


class EmDashExtension(Extension):
    """
    Extension that replaces '---' with '&emdash;'.
    """

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('emdashpattern', EmDashPattern(), '<not_strong')
