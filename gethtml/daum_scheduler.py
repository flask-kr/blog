# -*- coding=utf-8 -*-
from apscheduler.scheduler import Scheduler
from web.webtoon.model import WEBTOON, WEBTOON_DETAIL, db

sched = Scheduler()

# identify no  refined_detail[i][0]
@sched.interval_scheduler(days=1)
def update_data():
    refind_data, refined_detail = refined_data()
    for identify in refined_detail:
        webtoon = WEBTOON_DETAIL.query.filter(
            WEBTOON_DETAIL.chapter == identify[2],
            WEBTOON_DETAIL.identify_no == identify[1]
        )

        # if not webtoon:
        #     detail = WEBTOON_DETAIL(
        #         identify_no=identify[1],
        #         detail_no=identify[0],
        #         chapter=identify[2],
        #         list_title_url=identify[3],
        #         detail_url=identify[4]
        #     )
        #     db.session.add(detail)
        #     try:
        #         db.session.commit()
        #     except:
        #         db.session.rollback()


