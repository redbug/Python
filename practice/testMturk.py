'''
Created on Apr 14, 2011

@author: redbug
'''
from boto.mturk.connection import MTurkConnection, MTurkRequestError
from boto.mturk.qualification import Qualifications, \
    PercentAssignmentsApprovedRequirement, AdultRequirement
from boto.mturk.question import ExternalQuestion, QuestionForm, Overview, \
    Question, SimpleField, AnswerSpecification, FreeTextAnswer, Constraints, \
    QuestionContent, Binary, FormattedContent, SelectionAnswer
import datetime
from boto.resultset import ResultSet
from ImageChops import constant
from xml.dom.minidom import parseString

class MyMTurk:

    AWS_ACCESS_KEY_ID = 'skip'
    AWS_SECRET_ACCESS_KEY = 'skip'
    HOST_SANDBOX = 'mechanicalturk.sandbox.amazonaws.com'
    HOST_MTURK = 'mechanicalturk.amazonaws.com'

    EXTERNAL_URL = 'http://redbug0314.blogspot.com/p/imcrowd.html'

    def __init__( self ):
        #connect to MTurk
        self.connect = MTurkConnection( self.AWS_ACCESS_KEY_ID, self.AWS_SECRET_ACCESS_KEY, host=self.HOST_SANDBOX )

        #Qualification setting
        q = self.qualifications = Qualifications()

        # if required_to_preview == True unqualified user even can't view the hit.
#        q.add( PercentAssignmentsApprovedRequirement( comparator="GreaterThan", integer_value="95" ) )
        q.add( AdultRequirement( comparator="EqualTo", integer_value="1" ) )

    def register_hit_type( self ):
        try:
            reg_hit_type = self.connect.register_hit_type( title="Nine Picture!",
                                                           description="Choose some best pictures which you think is the best from following pictures.",
                                                           reward=0.01,
                                                           duration=60 * 30,
                                                           keywords="steak, photo",
                                                           approval_delay=datetime.timedelta( days=1 ),
                                                           qual_req=self.qualifications
                                                         )
        except MTurkRequestError as e:
            print "register hit type error:\n status: %s reason: %s\n body: %s" % ( e.status, e.reason, e.body )

        else:
            self.hit_type_id = reg_hit_type
            print "hit type id %s" % reg_hit_type


    def question_form( self ):

        qc = QuestionContent()
#        qc.append_field( 'Title', 'Is she hot?' )
        qc.append( Binary( 'image', 'jpg', 'http://www.miranchomeatmarket.com/images/T-%20bone%20steak.jpg', 'steak' ) )
        q = Question( identifier="This is the first girl!",
                      content=qc,
                      answer_spec=AnswerSpecification( FreeTextAnswer() ),
                      is_required=True,
                      display_name="This is display name" )
        qf = QuestionForm()
        qf.append( q )

        if self.hit_type_id:
            try:
                create_hit_rs = self.connect.create_hit( hit_type=self.hit_type_id,
                                                         question=qf,
                                                         lifetime=datetime.timedelta( days=14 ),
                                                         max_assignments=10,
                                                         annotation="This is a annotation"
                                                        )
            except MTurkRequestError as e:
                print "create hit type error:\n status: %s reason: %s\n body: %s" % ( e.status, e.reason, e.body )
            else:
                print "success!! key: %s" % create_hit_rs


    def question_form_formatted_content( self ):
        qc = QuestionContent()
        formatted_xhtml = """\
<table border="1">
  <tr>
    <td></td>
    <td align="center">1</td>
    <td align="center">2</td>
    <td align="center">3</td>
  </tr>
  <tr>
    <td align="right">A</td>
    <td align="center"><b>X</b></td>
    <td align="center">&nbsp;</td>
    <td align="center"><b>O</b></td>
  </tr>
  <tr>
    <td align="right">B</td>
    <td align="center">&nbsp;</td>
    <td align="center"><b>O</b></td>
    <td align="center">&nbsp;</td>
  </tr>
  <tr>
    <td align="right">C</td>
    <td align="center">&nbsp;</td>
    <td align="center">&nbsp;</td>
    <td align="center"><b>X</b></td>
  </tr>
  <tr>
    <td align="center" colspan="4">It is <b>X</b>'s turn.</td>
  </tr>
</table>
"""
        qc.append( FormattedContent( formatted_xhtml ) )

        q = Question( identifier="Formatted content test!",
                      content=qc,
                      answer_spec=AnswerSpecification( SelectionAnswer( min=1,
                                                                       max=5,
                                                                       style='checkbox',
                                                                       selections=[ ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcSh1HXq3WyOvvG7-AgvNugKC2LzImMUvUDNTuDAPwVKuw8NZzvLN62pGYhX:farm1.static.flickr.com/21/24204504_e143536a2e.jpg', 'steak1' ).get_as_xml(), 'img1' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcTkMoChevUBvQfmfksKDBM5oj4V2ruj6riqv7kC-_6qf9MR0igeBlJLkSI:www.miranchomeatmarket.com/images/T-%2520bone%2520steak.jpg', 'steak2' ).get_as_xml(), 'img2' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcSttsqT7kj9siDKZg1p4fU6W9IFlMZHCFSxFd49ECJR1Bu_1QlHQwmH1DU:img4.myrecipes.com/i/recipes/ck/06/08/grilled-steak-ck-1215910-l.jpg', 'steak3' ).get_as_xml(), 'img3' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcRfdQ-vuNt-W4W7JZRkAmbZpE6LLA0puCQs5erSzrGtsOY8H8t-vgEzqA:www.greendiamondgrille.com/images/new/NewYorkStripSteak.jpg', 'steak4' ).get_as_xml(), 'img4' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcTsJzCp6En1R9yvFQw7bGsSxiiQCqlMrFg7XCbcJ13G39Aa3e6ZilWW34oI:www.bunrab.com/dailyfeed/dailyfeed_images_jan-07/df07_01-08_steak.jpg', 'steak5' ).get_as_xml(), 'img5' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcTkMoChevUBvQfmfksKDBM5oj4V2ruj6riqv7kC-_6qf9MR0igeBlJLkSI:www.miranchomeatmarket.com/images/T-%2520bone%2520steak.jpg', 'steak2' ).get_as_xml(), 'img6' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcSttsqT7kj9siDKZg1p4fU6W9IFlMZHCFSxFd49ECJR1Bu_1QlHQwmH1DU:img4.myrecipes.com/i/recipes/ck/06/08/grilled-steak-ck-1215910-l.jpg', 'steak3' ).get_as_xml(), 'img7' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcRfdQ-vuNt-W4W7JZRkAmbZpE6LLA0puCQs5erSzrGtsOY8H8t-vgEzqA:www.greendiamondgrille.com/images/new/NewYorkStripSteak.jpg', 'steak4' ).get_as_xml(), 'img8' ),
                                                                                    ( Binary( 'image', 'jpg', 'http://images.google.com/images?q=tbn:ANd9GcTsJzCp6En1R9yvFQw7bGsSxiiQCqlMrFg7XCbcJ13G39Aa3e6ZilWW34oI:www.bunrab.com/dailyfeed/dailyfeed_images_jan-07/df07_01-08_steak.jpg', 'steak5' ).get_as_xml(), 'img9' )
                                                                                   ],
                                                                       type='binary'
                                                                       ) ),
                       is_required=True,
                       display_name="This is display name"
                     )

        qf = QuestionForm()
        qf.append( q )

        if self.hit_type_id:
            try:
                create_hit_rs = self.connect.create_hit( hit_type=self.hit_type_id,
                                                         question=qf,
                                                         lifetime=datetime.timedelta( days=14 ),
                                                         max_assignments=1,
                                                         annotation="This is a annotation"
                                                        )
            except MTurkRequestError as e:
                print "create hit type error:\n status: %s reason: %s\n body: %s" % ( e.status, e.reason, e.body )
            else:
                print "success!! key: %s" % create_hit_rs


    def external_question( self ):
        q = ExternalQuestion( external_url="http://www.kernel.org/pub/software/scm/git/docs/everyday.html", frame_height=200 )
#        keywords = ['image', 'filter', 'google']
#        #create hit without id
#        create_hit_rs = self.connect.create_hit( question=q, lifetime=60 * 65, max_assignments=2, title="Google Image Filter", keywords=keywords, reward=0.05, duration=60 * 6, approval_delay=60 * 60, annotation='An annotation from boto external question test', response_groups=['Minimal', 'HITDetail', 'HITQuestion', 'HITAssignmentSummary', ], qualifications=self.qualifications )

        #create hit with id
        if self.hit_type_id:
            try:
                hit = self.connect.create_hit( hit_type=self.hit_type_id,
                                                         question=q,
                                                         lifetime=datetime.timedelta( days=14 ),
                                                         max_assignments=1,
                                                         annotation="This is a annotation"
                                                        )

            except MTurkRequestError as e:
                print "register hit type error:\n status: %s reason: %s\n body: %s" % ( e.status, e.reason, e.body )
            else:
                print "hit id: %s " % hit[0].HITId
                print "hit type id: %s " % hit[0].HITTypeId

    def get_account_balance( self ):
        print self.connect.get_account_balance()

    def getHits( self ):
        print self.connect.get_all_hits()

    def getHit( self, hit_id ):
        hit_rs = self.connect.get_hit( hit_id )
        hit = hit_rs[0]
        for k, v in hit.__dict__.items():
            print "%s: %s" % ( k, v )

    def searchHits( self ):
        print self.connect.search_hits()

    def getAssignments( self, hit_id ):
        print self.connect.get_assignments( hit_id )

    def getReviewableHits( self ):
        print self.connect.get_reviewable_hits()

def main():
    myMTurk = MyMTurk()
#    myMTurk.getHit( '2HJ1K274J79KUL1XDWV6XXFCEYPEG4' )
#    myMTurk.getAssignments( '2HJ1K274J79KUL1XDWV6XXFCEYPEG4' )

#    myMTurk.getHits()


#    myMTurk.register_hit_type()
#    myMTurk.external_question()
#    myMTurk.get_account_balance()
#    myMTurk.question_form()
#    myMTurk.question_form_formatted_content()

#    myMTurk.searchHits()
#    myMTurk.getAssignments()
    myMTurk.getReviewableHits()

if __name__ == "__main__": main()

