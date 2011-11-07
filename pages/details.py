#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe <florin.strugariu@softvision.ro>
#                 David Burns
#                 Marc George
#                 Dave Hunt <dhunt@mozilla.com>
#                 Alex Rodionov <p0deje@gmail.com>
#                 Joel Andersson <janderssn@gmail.com>
#                 Marlena Compton <mcompton@mozilla.com>
#                 Teodosia Pop <teodosia.pop@softvision.ro>
#                 Alex Lakatos <alex@greensqr.com>
#                 Alin Trif <alin.trif@softvision.ro>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import re

from pages.page import Page
from pages.base import Base
from urllib2 import urlparse
from selenium.webdriver.common.by import By


class Details(Base):

    _breadcrumb_locator = (By.ID, "breadcrumbs")
    _current_page_breadcrumb_locator = (By.CSS_SELECTOR, "#breadcrumbs > ol > li:nth-child(3)")

    #addon informations
    _name_locator = (By.CSS_SELECTOR, "h1.addon")
    _title_locator = (By.CSS_SELECTOR, "#addon >hgroup> h1.addon")
    _version_number_locator = (By.CSS_SELECTOR, "span.version-number")
    _authors_locator = (By.XPATH, "//h4[@class='author']/a")
    _summary_locator = (By.ID, "addon-summary")
    _ratings_locator = (By.CSS_SELECTOR, "span[itemprop='rating']")
    _install_button_locator = (By.CSS_SELECTOR, "p[class='install-button'] > a")
    _contribute_button_locator = (By.CSS_SELECTOR, "a[id='contribute-button']")
    _rating_locator = (By.CSS_SELECTOR, "span[itemprop='rating']")
    _whats_this_license_locator = (By.CSS_SELECTOR, ".source > li:nth-child(2) > a")
    _description_locator = (By.CSS_SELECTOR, "div.prose")
    _register_link_locator = (By.CSS_SELECTOR, "li.account > a")
    _login_link_locator = (By.CSS_SELECTOR, "li.account > a:nth-child(2)")
    _other_applications_locator = (By.ID, "other-apps")
    _other_apps_dropdown_menu_locator = (By.CSS_SELECTOR, "ul.other-apps")

    _about_addon_locator = (By.CSS_SELECTOR, "section.primary > h2")
    _more_about_addon_locator = (By.ID, "more-about")
    _version_information_locator = (By.ID, "detail-relnotes")
    _version_information_heading_locator = (By.CSS_SELECTOR, "#detail-relnotes > h2")
    _release_version_locator = (By.CSS_SELECTOR, "div.info > h3 > a")
    _source_code_license_information_locator = (By.CSS_SELECTOR, ".source > li > a")
    _reviews_title_locator = (By.CSS_SELECTOR, "#reviews > h2")
    _tags_locator = (By.ID, "tagbox")
    _other_addons_header_locator = (By.CSS_SELECTOR, "h2.compact-bottom")
    _other_addons_list_locator = (By.CSS_SELECTOR, ".primary .listing-grid")
    _part_of_collections_locator = (By.CSS_SELECTOR, "#collections-grid")
    _icon_locator = (By.CSS_SELECTOR, "img.icon")
    _featured_image_locator = (By.CSS_SELECTOR, "#addon .featured .screenshot")
    _support_link_locator = (By.CSS_SELECTOR, "a.support")
    _review_details_locator = (By.CSS_SELECTOR, ".review .description")
    _all_reviews_link_locator = (By.CSS_SELECTOR, "a.more-info")
    _review_locator = (By.CSS_SELECTOR, "div.review:not(.reply)")
    _info_link_locator = (By.CSS_SELECTOR, "li > a.scrollto")
    _rating_counter_locator = (By.CSS_SELECTOR, ".grouped_ratings .num_ratings")
    _devs_comments_section_locator = (By.CSS_SELECTOR, "#developer-comments")

    _image_locator = (By.CSS_SELECTOR, "#preview.slider li.panel.active a")
    _image_viewer_locator = (By.ID, 'lightbox')

    #more about this addon
    _additional_images_locator = (By.CSS_SELECTOR, "#addon .article .screenshot")
    _website_locator = (By.CSS_SELECTOR, ".links a.home")
    #other_addons
    _other_addons_by_author_locator = (By.CSS_SELECTOR, "#author-addons")
    _reviews_locator = (By.ID, "reviews")
    _add_review_link_locator = (By.ID, "add-review")

    _add_to_collection_locator = (By.CSS_SELECTOR, ".collection-add.widget.collection")
    _add_to_collection_widget_locator = (By.CSS_SELECTOR, ".collection-add-login")
    _add_to_collection_widget_button_locator = (By.CSS_SELECTOR, ".register-button .button")
    _add_to_collection_widget_login_link_locator = (By.CSS_SELECTOR, ".collection-add-login a:nth-child(2)")

    _development_channel_locator = (By.CSS_SELECTOR, "#beta-channel")
#===============================================================================
# Webdriver Code
#===============================================================================

    def __init__(self, testsetup, addon_name=None):
        #formats name for url
        Base.__init__(self, testsetup)
        if (addon_name != None):
            self.addon_name = addon_name.replace(" ", "-")
            self.addon_name = re.sub(r'[^A-Za-z0-9\-]', '', self.addon_name).lower()
            self.addon_name = self.addon_name[:27]
            self.selenium.get("%s/addon/%s" % (self.base_url, self.addon_name))

    @property
    def _page_title(self):
        return "%s:: Add-ons for Firefox" % self.title

    @property
    def title(self):
        base = self.selenium.find_element(*self._title_locator).text
        version = self.selenium.find_element(self._title_locator[0], '%s > span' % self._title_locator[1]).text
        return base.replace(version, '')

    @property
    def has_reviews(self):
        return len(self.selenium.find_elements(*self._review_details_locator)) > 0

    def click_all_reviews_link(self):
        self.selenium.find_element(*self._all_reviews_link_locator).click()

    @property
    def review_count(self):
        return len(self.selenium.find_elements(*self._review_locator))

    @property
    def breadcrumb(self):
        return self.selenium.find_element(*self._breadcrumb_locator).text

    @property
    def current_page_breadcrumb(self):
        return self.selenium.find_element(*self._current_page_breadcrumb_locator).text

    @property
    def name(self):
        return self.selenium.find_element(*self._name_locator).text

    @property
    def version_number(self):
        return self.selenium.find_element(*self._version_number_locator).text

    @property
    def source_code_license_information(self):
        return self.selenium.find_element(*self._source_code_license_information_locator).text

    @property
    def authors(self):
        return [self.selenium.find_element(self._authors_locator[0], self._authors_locator[1] + "[ % s]" % (i + 1)).text
                for i in range(len(self.selenium.find_elements(*self._authors_locator)))]

    @property
    def summary(self):
        return self.selenium.find_element(*self._summary_locator).text

    @property
    def rating(self):
        return self.selenium.find_element(*self._rating_locator).text

    def click_whats_this_license(self):
        self.selenium.find_element(*self._whats_this_license_locator).click()
        from pages.addons_site import UserFAQ
        return UserFAQ(self.testsetup)

    @property
    def description(self):
        return self.selenium.find_element(*self._description_locator).text

    @property
    def register_link(self):
        return self.selenium.find_element(*self._register_link_locator).text

    @property
    def login_link(self):
        return self.selenium.find_element(*self._login_link_locator).text

    @property
    def other_apps(self):
        return self.selenium.find_element(*self._other_applications_locator).text

    @property
    def version_information_heading(self):
        return self.selenium.find_element(*self._version_information_heading_locator).text

    @property
    def version_information(self):
        return self.selenium.find_element(self._version_information_heading_locator[0], '%s > a' % self._version_information_heading_locator[1]).get_attribute('href')

    @property
    def release_version(self):
        return self.selenium.find_element(*self._release_version_locator).text

    @property
    def about_addon(self):
        return self.selenium.find_element(*self._about_addon_locator).text

    @property
    def review_title(self):
        return self.selenium.find_element(*self._reviews_title_locator).text

    @property
    def review_details(self):
        return self.selenium.find_element(*self._review_details_locator).text

    @property
    def often_used_with_header(self):
        return self.selenium.find_element(*self._other_addons_header_locator).text

    @property
    def devs_comments_title(self):
        return self.selenium.find_element(*self.append_value_to_locator(self._devs_comments_section_locator, "> h2")).text

    @property
    def devs_comments_message(self):
        return self.selenium.find_element(*self.append_value_to_locator(self._devs_comments_section_locator, "%s div.content")).text

    @property
    def is_register_visible(self):
        return self.is_element_visible(self._register_link_locator)

    @property
    def is_login_visible(self):
        return self.is_element_visible(self._login_link_locator)

    @property
    def is_other_apps_link_visible(self):
        return self.is_element_visible(self._other_applications_locator)

    @property
    def is_other_apps_dropdown_menu_visible(self):
        self.click_other_apps()
        return self.is_element_visible(self._other_apps_dropdown_menu_locator)

    @property
    def is_addon_name_visible(self):
        return self.is_element_visible(self._name_locator)

    @property
    def is_summary_visible(self):
        return self.is_element_visible(self._summary_locator)

    @property
    def is_about_addon_visible(self):
        return self.is_element_visible(self._about_addon_locator)

    @property
    def is_version_information_visible(self):
        return self.is_element_visible(self._version_information_locator)

    @property
    def is_version_information_heading_visible(self):
        return self.is_element_visible(self._version_information_heading_locator)

    def click_version_information_heading(self):
        return self.selenium.find_element(self._version_information_heading_locator[0], '%s > a' % self._version_information_heading_locator[1]).click()

    @property
    def is_version_information_section_expanded(self):
        expand_info = self.selenium.find_element(*self._version_information_locator).get_attribute("class")
        return ("expanded" in expand_info)

    @property
    def does_page_scroll_to_version_information_section(self):
        return (self.selenium.execute_script("window.pageYOffset")) > 2000

    @property
    def is_review_title_visible(self):
        return self.is_element_visible(self._reviews_title_locator)

    @property
    def is_often_used_with_header_visible(self):
        return self.is_element_visible(self._other_addons_header_locator)

    @property
    def is_often_used_with_list_visible(self):
        return self.is_element_visible(self._other_addons_list_locator)

    @property
    def are_tags_visible(self):
        return self.is_element_visible(self._tags_locator)

    @property
    def is_part_of_collections_header_visible(self):
        locator = (self._part_of_collections_locator[0], '%s h2 ' % self._part_of_collections_locator[1])
        return self.is_element_visible(locator)

    @property
    def is_part_of_collections_list_visible(self):
        locator = (self._part_of_collections_locator[0], '%s ul ' % self._part_of_collections_locator[1])
        return self.is_element_visible(locator)

    @property
    def is_devs_comments_section_visible(self):
        return self.is_element_visible(self._devs_comments_section_locator)

    def is_devs_comments_section_expanded(self):
        is_expanded = self.selenium.find_element(*self._devs_comments_section_locator).get_attribute("class")
        return ("expanded" in is_expanded)

    @property
    def part_of_collections_header(self):
        return self.selenium.find_element(self._part_of_collections_locator[0],
                                          '%s h2' % self._part_of_collections_locator[1]).text

    @property
    def part_of_collections_count(self):
        return len(self.selenium.find_elements(*"%s li" % self._part_of_collections_locator))

    def part_of_collections(self):
#        self.wait_for_element_present(self._part_of_collections_locator)
        return [self.PartOfCollectionsSnippet(self.testsetup, i) for i in range(self.part_of_collections_count)]

#===============================================================================
# Rc Code
#===============================================================================

    class PartOfCollectionsSnippet(Page):

        _collections_locator = "css=#collections-grid li"  # Base locator
        _name_locator = " div.summary > h3"
        _link_locator = " > a"

        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            self.lookup = lookup

        def absolute_locator(self, relative_locator):
            return self._root_locator + relative_locator

        @property
        def _root_locator(self):
            self.wait_for_element_visible(self._collections_locator)
            if type(self.lookup) == int:
                # lookup by index
                return "%s:nth(%s) > div" % (self._collections_locator, self.lookup)
            else:
                # lookup by name
                return "%s:contains(%s) > div" % (self._collections_locator, self.lookup)

        def click_collection(self):
            self.selenium.click(self.absolute_locator(self._link_locator))
            self.selenium.wait_for_page_to_load(self.timeout)
            from pages.collection import Collections
            return Collections(self.testsetup)

        @property
        def name(self):
            return self.selenium.get_text(self.absolute_locator(self._name_locator))
#===============================================================================
# Rc Code STOP
#===============================================================================

#===============================================================================
# Webdriver Code
#===============================================================================

    def click_other_apps(self):
        self.selenium.find_element(*self._other_applications_locator).click()
#        self.wait_for_element_visible(self._other_apps_dropdown_menu_locator)

    @property
    def icon_url(self):
        return self.selenium.find_element(*self._icon_locator).get_attribute('src')

    @property
    def website(self):
        return self.selenium.find_element(*self._website_locator).get_attribute('href')

    def click_website_link(self):
        self.selenium.find_element(*self._website_locator).click()

    @property
    def support_url(self):
        support_url = self.selenium.find_element(*self._support_link_locator).get_attribute('href')
        match = re.findall("http", support_url)
        #staging url
        if len(match) > 1:
            return self._extract_url_from_link(support_url)
        #production url
        else:
            return support_url

    def _extract_url_from_link(self, url):
        #parses out extra certificate stuff from urls in staging only
        return urlparse.unquote(re.search('\w+://.*/(\w+%3A//.*)', url).group(1))

    @property
    def other_addons_by_authors_text(self):
        return self.selenium.find_element(self._other_addons_by_author_locator[0], "%s > h2" % self._other_addons_by_author_locator[1]).text

    @property
    def other_addons(self):
        return [self.OtherAddons(self.testsetup, element) for element in self.selenium.find_elements(*self._other_addons_by_author_locator)]

    def get_rating_counter(self, rating):
        if rating == 1:
            locator = "%s:nth(4)" % self._rating_counter_locator[1]
        elif rating == 2:
            locator = "%s:nth(3)" % self._rating_counter_locator[1]
        elif rating == 3:
            locator = "%s:nth(2)" % self._rating_counter_locator[1]
        elif rating == 4:
            locator = "%s:nth(1)" % self._rating_counter_locator[1]
        elif rating == 5:
            locator = "%s:nth(0)" % self._rating_counter_locator[1]
        else:
            raise RuntimeError("No such rating %s!" % str(rating))
        return int(self.selenium.find_element(self._rating_counter_locator[0], locator).text)

    @property
    def previewer(self):
        return self.ImagePreviewer(self.testsetup)

    def click_add_to_collection_widget(self):
        self.selenium.find_element(*self._add_to_collection_locator).click()

    @property
    def is_collection_widget_visible(self):
        return self.is_element_visible(self._add_to_collection_widget_locator)

    @property
    def is_collection_widget_button_visible(self):
        return self.is_element_visible(self._add_to_collection_widget_button_locator)

    @property
    def collection_widget_button(self):
        return self.selenium.find_element(*self._add_to_collection_widget_button_locator).text

    @property
    def is_collection_widget_login_link_visible(self):
        return self.is_element_visible(self._add_to_collection_widget_login_link_locator)

    @property
    def collection_widget_login_link(self):
        return self.selenium.find_element(*self._add_to_collection_widget_login_link_locator).text

    class ImagePreviewer(Page):

        #navigation
        _next_locator = (By.CSS_SELECTOR, 'section.previews.carousel > a.next')
        _prev_locator = (By.CSS_SELECTOR, 'section.previews.carousel > a.prev')

        _image_locator = (By.CSS_SELECTOR, '#preview')

        def next_set(self):
            self.selenium.find_element(*self._next_locator).click()

        def prev_set(self):
            self.selenium.find_element(*self._prev_locator).click()

        def click_image(self, image_no=0):
            self.selenium.find_element(self._image_locator[0],
                        '%s li:nth-child(%s) a' % (self._image_locator[1], image_no + 1)).click()
            from pages.regions.image_viewer import ImageViewer
            image_viewer = ImageViewer(self.testsetup)
            #image_viewer.wait_for_image_viewer_to_finish_animating()
            return image_viewer

        def image_title(self, image_no):
            return self.selenium.find_element(self._image_locator[0],
                        '%s li:nth-child(%s) a' % (self._image_locator[1], image_no + 1)).get_attribute('title')

        def image_link(self, image_no):
            return self.selenium.find_element(self._image_locator[0],
                        '%s li:nth-child(%s) a img' % (self._image_locator[1], image_no + 1)).get_attribute('src')

        @property
        def image_count(self):
            return len(self.selenium.find_elements(self._image_locator[0], '%s li' % self._image_locator[1]))

        @property
        def image_set_count(self):
            if self.image_count % 3 == 0:
                return self.image_count / 3
            else:
                return self.image_count / 3 + 1

    def review(self, lookup):
        return self.DetailsReviewSnippet(self.testsetup, lookup)

    def reviews(self):
        return [self.DetailsReviewSnippet(self.testsetup, i) for i in range(self.reviews_count)]

    @property
    def reviews_count(self):
#        self.wait_for_element_visible(self._reviews_locator)
        return len(self.selenium.find_elements(*self._reviews_locator))

    @property
    def version_info_link(self):
        return self.selenium.find_element(*self._info_link_locator).get_ttribute("href")

    @property
    def is_version_info_link_visible(self):
        return self.is_element_visible(self._info_link_locator)

    def click_version_info_link(self):
        self.selenium.find_element(*self._info_link_locator).click()

    def click_devs_comments_title(self):
        self.selenium.find_element(self._devs_comments_section_locator[0], "%s > h2 > a" % self._devs_comments_section_locator[1]).click()

    class OtherAddons(Page):
        _other_addons_locator = (By.CSS_SELECTOR, '#author-addons li')
        _name_locator = (By.CSS_SELECTOR, 'div.summary h3')
        _addon_link_locator = (By.CSS_SELECTOR, 'div.addon > a')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
#            self.selenium.mouse_over(self.absolute_locator(self._name_locator))
            return self._root_element.find_element(*self._name_locator).text

        def click_addon_link(self):
            self._root_element.find_element(*self._addon_link_locator).click()

        @property
        def name_link_value(self):
            return self._root_element.find_element(*self._name_link_locator).get_attribute('href')

    class DetailsReviewSnippet(Page):

        _reviews_locator = (By.CSS_SELECTOR, '#reviews div')  # Base locator
        _username_locator = (By.CSS_SELECTOR, 'p.byline a')

        def __init__(self, testsetup, lookup):
            Page.__init__(self, testsetup)
            self.lookup = lookup

        def absolute_locator(self, relative_locator):
            return self._root_locator + relative_locator

        @property
        def _root_locator(self):
            self.wait_for_element_visible(self._reviews_locator)
            if type(self.lookup) == int:
                # lookup by index
                return "%s:nth(%s) " % (self._reviews_locator, self.lookup)
            else:
                # lookup by name
                return "%s:contains(%s) " % (self._reviews_locator, self.lookup)

        @property
        def username(self):
            return self.selenium.get_text(self.absolute_locator(self._username_locator))

        def click_username(self):
            self.selenium.click(self.absolute_locator(self._username_locator))
            self.selenium.wait_for_page_to_load(self.timeout)
            from pages.user import User
            return User(self.testsetup)

#===============================================================================
# Webdriver Code
#==============================================================================
#===============================================================================
# Rc Code
#===============================================================================
    def click_to_write_review(self):
        self.selenium.find_element(*self._add_review_link_locator).click()
        from pages.addons_site import WriteReviewBlock
        return WriteReviewBlock(self.testsetup)

    @property
    def development_channel_text(self):
        return self.selenium.find_element(self._development_channel_locator[0], '%s > h2' % self._development_channel_locator[1]).text

    @property
    def is_development_channel_header_visible(self):
        return self.is_element_visible(self._development_channel_locator[0], '%s > h2' % self._development_channel_locator[1])

    def click_development_channel(self):
        self.selenium.find_element(self._development_channel_locator[0], '%s > h2 > a' % self._development_channel_locator[1]).click()

    @property
    def is_development_channel_expanded(self):
        is_expanded = self.selenium.find_element(*self._development_channel_locator).get_attribute('class')
        return "expanded" in is_expanded

    @property
    def is_development_channel_content_visible(self):
        return self.is_element_visible(self._development_channel_locator[0], '%s > div' % self._development_channel_locator[1])
