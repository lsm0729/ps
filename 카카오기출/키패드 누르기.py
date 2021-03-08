class Thumb(object):

    def __init__(self,hand):
        hand = 0 if hand=="left" else 1
        default_hand = 'L' if hand==0 else 'R'
        self.hand_in_str      = default_hand
        self.hand             = hand
        self.current_hand_pos = [10,11] ## 왼손오른손 초기상태     왼 * 오 #
        self.split            = {1:0,4:0,7:0,3:1,6:1,9:1,2:2,5:2,8:2,0:2}    ## 1,4,7 왼손 0   3,6,9 오른손 1   2,5,8,0  중간 2
        self.answer           = ''
        self.mmap             = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),10:(3,0),0:(3,1),11:(3,2)}  ## 번호들의 좌표 dict로 저장

    def move(self,next):
        if self.split[next]==0:
            #print(str(next)+' lefthand')
            self.current_hand_pos[0]=next
            #print(self.current_hand_pos)
            self.answer+='L'
        elif self.split[next]==1:
            #print(str(next)+' righthand')
            self.current_hand_pos[1]=next
            #print(self.current_hand_pos)
            self.answer+='R'
        ##TODO: 중간 숫자
        else:
            l_y,l_x       = self.mmap[self.current_hand_pos[0]]
            r_y,r_x       = self.mmap[self.current_hand_pos[1]]
            next_y,next_x = self.mmap[next]

            dist_from_left  = abs(next_y-l_y)+abs(next_x-l_x)
            dist_from_right = abs(next_y-r_y)+abs(next_x-r_x)


            if dist_from_left == dist_from_right:
                #print(str(next) + ' dist same {}'.format(self.hand_in_str))
                self.current_hand_pos[self.hand]=next
                #print(self.current_hand_pos)
                self.answer+=self.hand_in_str

            elif dist_from_left<dist_from_right:
                #print(str(next)+' lefthand')
                self.current_hand_pos[0]=next
                #print(self.current_hand_pos)
                self.answer+='L'

            else:
                #print(str(next)+' righthand')
                self.current_hand_pos[1]=next
                #print(self.current_hand_pos)
                self.answer+='R'

    def pos(self,next):

        y,x = self.mmap[next]
        #print(y,x)

    def __repr__(self):
        return str(self.hand_in_str)+' '+str(self.hand)+' '+str(self.current_hand_pos[0])+' '+str(self.current_hand_pos[1])+' '+str(self.answer)+' '+str(self.split)+' '+str(self.mmap)+'\n'







def solution(numbers, hand):
    thumb = Thumb(hand)

    for x in numbers:
        thumb.move(x)

    return thumb.answer