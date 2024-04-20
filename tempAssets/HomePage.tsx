import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import { FrameIcon2 } from './FrameIcon2.js';
import { FrameIcon3 } from './FrameIcon3.js';
import { FrameIcon4 } from './FrameIcon4.js';
import { FrameIcon } from './FrameIcon.js';
import classes from './HomePage.module.css';

interface Props {
  className?: string;
}
/* @figmaId 18:1001 */
export const HomePage: FC<Props> = memo(function HomePage(props = {}) {
  return (
    <div className={`${resets.storybrainResets} ${classes.root}`}>
      <div className={classes.createAScreenBasedOnTitleJungl}>
        <div className={classes.frame}>
          <div className={classes.frame2}>
            <div className={classes.frame3}>
              <div className={classes.frame4}>
                <div className={classes.leaderboards}>Leaderboards</div>
              </div>
            </div>
            <div className={classes.frame5}>
              <FrameIcon className={classes.icon} />
            </div>
          </div>
          <div className={classes.frame6}>
            <div className={classes.frame7}>
              <div className={classes.frame8}>
                <div className={classes.stats}>Stats</div>
              </div>
            </div>
            <div className={classes.frame9}>
              <FrameIcon2 className={classes.icon2} />
            </div>
          </div>
        </div>
        <div className={classes.frame10}>
          <div className={classes.frame11}>
            <div className={classes.quickLinks}>Quick Links</div>
          </div>
        </div>
        <div className={classes.frame12}>
          <div className={classes.frame13}>
            <div className={classes.frame14}>
              <div className={classes.frame15}>
                <div className={classes.frame16}>
                  <div className={classes.startNow}>Start Now</div>
                </div>
                <div className={classes.frame17}>
                  <div className={classes.frame18}>
                    <div className={classes.frame19}>
                      <div className={classes.reward30Leaves}>Reward: 30 leaves</div>
                    </div>
                    <div className={classes.frame20}>
                      <div className={classes.completeA5kRunThroughVirtualRa}>
                        Complete a 5k run through virtual rainforest
                      </div>
                    </div>
                  </div>
                  <div className={classes.frame21}>
                    <div className={classes.rainforestRun}>Rainforest Run</div>
                  </div>
                </div>
              </div>
            </div>
            <div className={classes.frame22}>
              <div className={classes.frame23}></div>
            </div>
          </div>
        </div>
        <div className={classes.frame24}>
          <div className={classes.frame25}>
            <div className={classes.frame26}>
              <div className={classes.frame27}>
                <div className={classes.startNow2}>Start Now</div>
              </div>
              <div className={classes.frame28}>
                <div className={classes.frame29}>
                  <div className={classes.frame30}>
                    <div className={classes.reward30Leaves2}>Reward: 30 leaves</div>
                  </div>
                  <div className={classes.frame31}></div>
                </div>
                <div className={classes.completeThisSideQuestByLifting}>
                  Complete this side quest by lifting weights for 30 minutes
                </div>
                <div className={classes.frame32}>
                  <div className={classes.gymFor30Minutes}>Gym for 30 minutes</div>
                </div>
              </div>
            </div>
          </div>
          <div className={classes.frame33}>
            <div className={classes.frame34}></div>
          </div>
        </div>
        <div className={classes.frame35}>
          <div className={classes.frame36}>
            <div className={classes.frame37}>
              <div className={classes._82Km}>8.2 km</div>
            </div>
            <div className={classes.frame38}>
              <div className={classes.distance}>Distance</div>
            </div>
          </div>
          <div className={classes.frame39}>
            <div className={classes.frame40}>
              <div className={classes._10450Steps}>10450 Steps</div>
            </div>
            <div className={classes.frame41}>
              <div className={classes.dailySteps}>Daily Steps</div>
            </div>
          </div>
          <div className={classes.frame42}>
            <div className={classes.frame43}>
              <div className={classes.dailyJungleChallenge}>Daily Jungle Challenge</div>
            </div>
          </div>
        </div>
        <div className={classes.frame44}>
          <div className={classes.frame45}>
            <div className={classes._575Kcal}>575 Kcal</div>
          </div>
          <div className={classes.frame46}>
            <div className={classes.caloriesBurned}>Calories Burned</div>
          </div>
        </div>
        <div className={classes.frame47}>
          <div className={classes.frame48}>
            <div className={classes.frame49}>
              <div className={classes._98ToLvl21}>98% to Lvl 21</div>
            </div>
            <div className={classes.frame50}>
              <div className={classes.lvl20Jaguar}>Lvl 20 Jaguar</div>
            </div>
            <div className={classes.frame51}>
              <div className={classes.explorerLeo}>Explorer Leo</div>
            </div>
          </div>
          <div className={classes.frame52}></div>
        </div>
        <div className={classes.frame53}>
          <div className={classes.frame54}></div>
          <div className={classes.frame55}>
            <div className={classes.frame56}>
              <div className={classes.frame57}>
                <FrameIcon3 className={classes.icon3} />
              </div>
            </div>
            <div className={classes.frame58}>
              <div className={classes.frame59}>
                <FrameIcon4 className={classes.icon4} />
              </div>
            </div>
          </div>
        </div>
        <div className={classes.jungleDashboard}>Jungle Dashboard</div>
      </div>
    </div>
  );
});
