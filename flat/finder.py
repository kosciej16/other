#!/usr/bin/env python
# -*- coding: utf8 -*-

import ConfigParser
import smtplib
import sys
import time
import urllib2
from abc import abstractmethod
from urlparse import urlparse

from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')
htmlparser = etree.HTMLParser()


class Rule(object):

    def __init__(self, xpath):
        self.xpath = xpath

    @classmethod
    def to_int(cls, s):
        res = '0'
        for c in s:
            if c.isdigit():
                res += c
        return int(res)

    @abstractmethod
    def check(self, tree):
        pass


class WordRule(Rule):

    def __init__(self, xpath, words):
        super(WordRule, self).__init__(xpath)
        self.words = words

    def check(self, tree):
        offer_word = tree.xpath(self.xpath)[0].lower()
        for word in [w.lower() for w in self.words]:
            if word in offer_word:
                return True
        return False


class NumberRule(Rule):

    def __init__(self, xpath, lower, upper):
        super(NumberRule, self).__init__(xpath)
        self.lower = lower
        self.upper = upper

    def check(self, tree):
        tmp = tree.xpath(self.xpath)
        if not tmp: return False
        offer_number = Rule.to_int(tree.xpath(self.xpath)[0])
        if self.upper >= offer_number and self.lower <= offer_number:
            return True
        return False


class STMPWrapper(object):

    def __init__(self, conf):
        """
        @type conf: ConfigParser
        """
        self.conf = conf
        self.smtp = self.conf.get('smtp', 'smtp')
        self.port = int(self.conf.get('smtp', 'port'))
        self.sender = conf.get('smtp', 'from')
        self.rec = conf.get('smtp', 'to')
        self.username = conf.get('smtp', 'username')
        self.password = conf.get('smtp', 'password')
        self.connected = False

    def connect(self):
        if not self.connected:
            self.server = smtplib.SMTP("{}:{}".format(self.smtp, self.port))
            self.server.ehlo()
            self.server.starttls()
            self.connected = True

    def login(self):
        self.server.login(self.username, self.password)

    def sendmail(self, content):
        message = """From: {}\nTo: {}\nSubject: {}\n\n{}""".format(
            self.sender, self.rec, "MIESZKANIA", content)
        if content:
            self.server.sendmail(self.sender, [self.rec], message)


class Finder(object):

    def __init__(self, cfg_name):
        """
        @type cfg_name: str
        """
        self.conf = ConfigParser.RawConfigParser()
        self.conf.read(cfg_name)
        self.from_config(self.conf)
        self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.url))
        self.tree = etree.parse(urllib2.urlopen(self.url), htmlparser)
        self.processed_urls = self.get_processed_urls()
        self.connect_smtp()

    def from_config(self, conf):
        """
        @type conf: ConfigParser
        """
        self.url = conf.get('general', 'url')
        self.offers = conf.get('general', 'offers')
        self.parse_rules(conf)

    def get_processed_urls(self):
        self.processed_urls_file = open("processed_urls", "a+")
        return self.processed_urls_file.read().split('\n')

    def connect_smtp(self):
        self.smtp_wrapper = STMPWrapper(self.conf)
        self.smtp_wrapper.connect()
        self.smtp_wrapper.login()

    def parse_rules(self, conf):
        self.rules = []
        for section in conf.sections():
            if section.startswith('rule'):
                if conf.has_option(section, 'word'):
                    self.rules.append(WordRule(
                        conf.get(section, 'xpath'), conf.get(section, 'word').split(',')))
                else:
                    lower = 0
                    upper = 100000
                    if conf.has_option(section, 'upper'):
                        upper = int(conf.get(section, 'upper'))
                    if conf.has_option(section, 'lower'):
                        lower = int(conf.get(section, 'lower'))
                    self.rules.append(NumberRule(conf.get(section, 'xpath'), lower, upper))

    def sendmail(self, content):
        print "sending email with %d offers" % len(content.splitlines())
        self.smtp_wrapper.sendmail(content)

    def run(self):
        while True:
            hrefs = self.tree.xpath(self.offers)
            content = ''
            for href in hrefs:
                full_url = self.domain + href
                if full_url in self.processed_urls:
                    continue
                print "processing url %s" % full_url
                self.processed_urls.append(full_url)
                self.processed_urls_file.write(full_url + '\n')
                try:
                    tree = etree.parse(urllib2.urlopen(full_url), htmlparser)
                except urllib2.HTTPError:
                    continue
                acc = True
                for rule in self.rules:
                    if not rule.check(tree):
                        acc = False
                        break
                if acc:
                    content += full_url + '\n'
            self.sendmail(content)
            self.processed_urls_file.flush()
            time.sleep(60)


if __name__ == "__main__":
    Finder('config').run()
