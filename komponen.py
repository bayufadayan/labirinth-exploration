from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

def Component():
  Batu_001 = Entity (
      model = 'assets/Stone/dirty_stones_pile.glb',
      position = (10, 0, 6),
      scale = (0.3),
  )
  Batu_002 = duplicate (
      Batu_001,
      position = (-10, 0, -7),
      scale = (0.3),
  )
  Batu_003 = duplicate (
      Batu_001,
      position = (6, 0, -12),
      scale = (0.3),
  )
  Batu_004 = duplicate (
      Batu_001,
      position = (-6, 0, -17),
      scale = (0.3),
  )
  Batu_005 = duplicate (
      Batu_001,
      position = (9, 0, -10),
        scale = (0.3),
  )
  Batu_006 = duplicate (
    Batu_001,
      position = (15, 0, -14),
      scale = (0.3),
  )
  Batu_007 = duplicate (
    Batu_001,
      position = (-9, 0, -22),
      scale = (0.3),
  )
  Batu_008 = duplicate (
    Batu_001,
      position = (19, 0, -16),
      scale = (0.3),
  )
  Batu_009 = duplicate (
    Batu_001,
      position = (10, 0, -7),
      scale = (0.3),
  )
  Batu_010 = duplicate (
    Batu_001,
      position = (15, 0, -2),
      scale = (0.3),
  )
  Batu_011 = duplicate (
    Batu_001,
      position = (29, 0, -9),
      scale = (0.3),
  )
  Batu_012 = duplicate (
    Batu_001,
      position = (27, 0, -12),
      scale = (0.3),
  )
  Batu_013 = duplicate (
    Batu_001,
      position = (24, 0, -22),
      scale = (0.3),
  )
  Batu_014 = duplicate (
    Batu_001,
      position = (29, 0, -28),
      scale = (0.3),
  )
  Batu_015 = duplicate (
    Batu_001,
      position = (18, 0, -28),
      scale = (0.3),
  )
  Batu_016 = duplicate (
    Batu_001,
      position = (-9, 0, -28),
      scale = (0.3),
  )
  Batu_017 = duplicate (
    Batu_001,
      position = (-19, 0, -28),
      scale = (0.3),
  )
  Batu_018 = duplicate (
    Batu_001,
      position = (-26, 0, -28),
      scale = (0.3),
  )
  Batu_019 = duplicate (
    Batu_001,
      position = (-36, 0, -28),
      scale = (0.3),
  )
  Batu_020 = duplicate (
    Batu_001,
      position = (-27, 0, -21),
      scale = (0.3),
  )
  Batu_021 = duplicate (
    Batu_001,
      position = (-13, 0, -17),
      scale = (0.3),
  )
  Batu_022 = duplicate (
    Batu_001,
      position = (-27, 0, -9),
      scale = (0.3),
  )
  Batu_023 = duplicate (
    Batu_001,
      position = (-18, 0, -2.5),
      scale = (0.3),
  )
  Batu_024 = duplicate (
    Batu_001,
      position = (-21, 0, -4.5),
      scale = (0.3),
  )
  Batu_025 = duplicate (
    Batu_001,
      position = (-39, 0, -12),
      scale = (0.3),
  )
  Batu_026 = duplicate (
    Batu_001,
      position = (-43, 0, -9),
      scale = (0.3),
  )
  Batu_027 = duplicate (
    Batu_001,
      position = (-44, 0, 4),
      scale = (0.3),
  )
  Batu_028 = duplicate (
    Batu_001,
      position = (-44, 0, 11.5),
      scale = (0.3),
  )
  Batu_029 = duplicate (
    Batu_001,
      position = (-44, 0, 20),
      scale = (0.3),
  )
  Batu_030 = duplicate (
    Batu_001,
      position = (-42, 0, 29),
      scale = (0.3),
  )
  Batu_031 = duplicate (
    Batu_001,
      position = (-39, 0, 16),
      scale = (0.3),
  )
  Batu_032 = duplicate (
    Batu_001,
      position = (-27, 0, 16),
      scale = (0.3),
  )
  Batu_033 = duplicate (
    Batu_001,
      position = (-25, 0, 23),
      scale = (0.3),
  )
  Batu_034 = duplicate (
    Batu_001,
      position = (-23, 0, 30),
      scale = (0.3),
  )
  Batu_035 = duplicate (
    Batu_001,
      position = (-13.5, 0, 11),
      scale = (0.3),
  )
  Batu_036 = duplicate (
    Batu_001,
      position = (-1, 0, 22),
      scale = (0.3),
  )
  Batu_037 = duplicate (
    Batu_001,
      position = (-20, 0, 29),
      scale = (0.3),
  )
  Batu_038 = duplicate (
    Batu_001,
      position = (5, 0, 17),
      scale = (0.3),
  )
  Batu_039 = duplicate (
    Batu_001,
      position = (8, 0, 14),
      scale = (0.3),
  )
  Batu_040 = duplicate (
    Batu_001,
      position = (14, 0, 11),
      scale = (0.3),
  )
  Batu_041 = duplicate (
    Batu_001,
      position = (19, 0, 6),
      scale = (0.3),
  )
  Batu_042 = duplicate (
    Batu_001,
      position = (21, 0, 22),
      scale = (0.3),
  )
  Batu_043 = duplicate (
    Batu_001,
      position = (24, 0, 14),
      scale = (0.3),
  )
  Batu_044 = duplicate (
    Batu_001,
      position = (29, 0, 10),
      scale = (0.3),
  )
  Batu_045 = duplicate (
    Batu_001,
      position = (29, 0, 29),
      scale = (0.3),
  )
  Batu_046 = duplicate (
    Batu_001,
      position = (-52, 0, -44),
      scale = (0.3),
  )
  Batu_047 = duplicate (
    Batu_001,
      position = (-52, 0, -60),
      scale = (0.3),
  )
  Batu_048 = duplicate (
    Batu_001,
      position = (-52, 0, -73),
      scale = (0.3),
  )
  Batu_049 = duplicate (
    Batu_001,
      position = (-52, 0, -77),
      scale = (0.3),
  )
  Batu_050 = duplicate (
    Batu_001,
      position = (-52, 0, -85),
      scale = (0.3),
  )
  Batu_051 = duplicate (
    Batu_001,
      position = (-50, 0, -52),
      scale = (0.3),
  )
  Batu_052 = duplicate (
    Batu_001,
      position = (-44, 0, -44),
      scale = (0.3),
  )
  Batu_053 = duplicate (
    Batu_001,
      position = (-39, 0, -43),
      scale = (0.3),
  )
  Batu_054 = duplicate (
    Batu_001,
      position = (-40, 0, -55),
      scale = (0.3),
  )
  Batu_055 = duplicate (
    Batu_001,
      position = (-38, 0, -71),
      scale = (0.3),
  )
  Batu_056 = duplicate (
    Batu_001,
      position = (-38, 0, -79),
      scale = (0.3),
  )
  Batu_057 = duplicate (
    Batu_001,
      position = (-32, 0, -32),
      scale = (0.3),
  )
  Batu_058 = duplicate (
    Batu_001,
      position = (-32, 0, -49),
      scale = (0.3),
  )
  Batu_059 = duplicate (
    Batu_001,
      position = (-32, 0, -53),
      scale = (0.3),
  )
  Batu_060 = duplicate (
    Batu_001,
      position = (-34, 0, -65),
      scale = (0.3),
  )
  Batu_061 = duplicate (
    Batu_001,
      position = (-34, 0, -79),
      scale = (0.3),
  )
  Batu_062 = duplicate (
    Batu_001,
      position = (-32, 0, -85),
      scale = (0.3),
  )
  Batu_063 = duplicate (
    Batu_001,
      position = (-28, 0, -85),
      scale = (0.3),
  )
  Batu_064   = duplicate (
    Batu_001,
      position = (-27, 0, -37),
      scale = (0.3),
  )
  Batu_065   = duplicate (
    Batu_001,
      position = (-26, 0, -65),
      scale = (0.3),
  )
  Batu_066   = duplicate (
    Batu_001,
      position = (-22, 0, -79),
      scale = (0.3),
  )
  Batu_067   = duplicate (
    Batu_001,
      position = (-22, 0, -60),
      scale = (0.3),
  )
  Batu_068   = duplicate (
    Batu_001,
      position = (-22, 0, -48),
      scale = (0.3),
  )
  Batu_069   = duplicate (
    Batu_001,
      position = (-14, 0, -55),
      scale = (0.3),
  )
  Batu_070   = duplicate (
    Batu_001,
      position = (-16, 0, -65),
      scale = (0.3),
  )
  Batu_071   = duplicate (
    Batu_001,
      position = (-19, 0, -85),
      scale = (0.3),
  )
  Batu_072   = duplicate (
    Batu_001,
      position = (-14, 0, -79),
      scale = (0.3),
  )
  Batu_073   = duplicate (
    Batu_001,
      position = (-10, 0, -32),
      scale = (0.3),
  )
  Batu_074   = duplicate (
    Batu_001,
      position = (-8, 0, -43),
      scale = (0.3),
  )
  Batu_075   = duplicate (
    Batu_001,
      position = (-8, 0, -47),
      scale = (0.3),
  )
  Batu_076   = duplicate (
    Batu_001,
      position = (-8, 0, -61),
      scale = (0.3),
  )
  Batu_077   = duplicate (
    Batu_001,
      position = (-10, 0, -71),
      scale = (0.3),
  )
  Batu_078   = duplicate (
    Batu_001,
      position = (-8, 0, -85),
      scale = (0.3),
  )
  Batu_079   = duplicate (
    Batu_001,
      position = (-4, 0, -85),
      scale = (0.3),
  )
  Batu_080   = duplicate (
    Batu_001,
      position = (-4, 0, -44),
      scale = (0.3),
  )
  Batu_081   = duplicate (
    Batu_001,
      position = (-4, 0, -54),
      scale = (0.3),
  )
  Batu_082   = duplicate (
    Batu_001,
      position = (-2, 0, -66),
      scale = (0.3),
  )
  Batu_083   = duplicate (
    Batu_001,
      position = (-2, 0, -77),
      scale = (0.3),
  )
  Batu_084   = duplicate (
    Batu_001,
      position = (2, 0, -44),
      scale = (0.3),
  )
  Batu_085   = duplicate (
    Batu_001,
      position = (2, 0, -70),
      scale = (0.3),
  )
  Batu_086   = duplicate (
    Batu_001,
      position = (2, 0, -74),
      scale = (0.3),
  )
  Batu_087   = duplicate (
    Batu_001,
      position = (4, 0, -85),
      scale = (0.3),
  )
  Batu_088   = duplicate (
    Batu_001,
      position = (4, 0, -54),
      scale = (0.3),
  )
  Batu_089   = duplicate (
    Batu_001,
      position = (4, 0, -34),
      scale = (0.3),
  )
  Batu_090   = duplicate (
    Batu_001,
      position = (8, 0, -35),
      scale = (0.3),
  )
  Batu_091   = duplicate (
    Batu_001,
      position = (8, 0, -53),
      scale = (0.3),
  )
  Batu_092   = duplicate (
    Batu_001,
      position = (8, 0, -61),
      scale = (0.3),
  )
  Batu_093   = duplicate (
    Batu_001,
      position = (8, 0, -65),
      scale = (0.3),
  )
  Batu_094   = duplicate (
    Batu_001,
      position = (8, 0, -79),
      scale = (0.3),
  )
  Batu_095   = duplicate (
    Batu_001,
      position = (8, 0, -83),
      scale = (0.3),
  )
  Batu_096   = duplicate (
    Batu_001,
      position = (14, 0, -73),
      scale = (0.3),
  )
  Batu_097   = duplicate (
    Batu_001,
      position = (10, 0, -49),
      scale = (0.3),
  )
  Batu_098   = duplicate (
    Batu_001,
      position = (14, 0, -49),
      scale = (0.3),
  )
  Batu_099   = duplicate (
    Batu_001,
      position = (16, 0, -55),
      scale = (0.3),
  )
  Batu_100   = duplicate (
    Batu_001,
      position = (15, 0, -59),
      scale = (0.3),
  )
  Batu_101   = duplicate (
    Batu_001,
      position = (16, 0, -77),
      scale = (0.3),
  )
  Batu_102   = duplicate (
    Batu_001,
      position = (22, 0, -85),
      scale = (0.3),
  )
  Batu_103   = duplicate (
    Batu_001,
      position = (20, 0, -65),
      scale = (0.3),
  )
  Batu_104   = duplicate (
    Batu_001,
      position = (20, 0, -53),
      scale = (0.3),
  )
  Batu_105   = duplicate (
    Batu_001,
      position = (20, 0, -35),
      scale = (0.3),
  )
  Batu_106   = duplicate (
    Batu_001,
      position = (22, 0, -49),
      scale = (0.3),
  )
  Batu_107   = duplicate (
    Batu_001,
      position = (26, 0, -45),
      scale = (0.3),
  )
  Batu_108   = duplicate (
    Batu_001,
      position = (26, 0, -85),
      scale = (0.3),
  )
  Batu_109   = duplicate (
    Batu_001,
      position = (28, 0, -55),
      scale = (0.3),
  )
  Batu_110   = duplicate (
    Batu_001,
      position = (30, 0, -41),
      scale = (0.3),
  )
  Batu_111   = duplicate (
    Batu_001,
      position = (32, 0, -73),
      scale = (0.3),
  )
  Batu_112   = duplicate (
    Batu_001,
      position = (32, 0, -55),
      scale = (0.3),
  )
  Batu_113   = duplicate (
    Batu_001,
      position = (33, 0, -17),
      scale = (0.3),
  )
  Batu_114   = duplicate (
    Batu_001,
      position = (33, 0, -31),
      scale = (0.3),
  )
  Batu_115   = duplicate (
    Batu_001,
      position = (35, 0, -59),
      scale = (0.3),
  )
  Batu_116   = duplicate (
    Batu_001,
      position = (35, 0, -37),
      scale = (0.3),
  )
  Batu_117   = duplicate (
    Batu_001,
      position = (41, 0, -31),
      scale = (0.3),
  )
  Batu_118   = duplicate (
    Batu_001,
      position = (40, 0, -47),
      scale = (0.3),
  )
  Batu_119   = duplicate (
    Batu_001,
      position = (40, 0, -49),
      scale = (0.3),
  )
  Batu_120   = duplicate (
    Batu_001,
      position = (40, 0, -61),
      scale = (0.3),
  )
  Batu_121   = duplicate (
    Batu_001,
      position = (40, 0, -65),
      scale = (0.3),
  )
  Batu_122   = duplicate (
    Batu_001,
      position = (40, 0, -71),
      scale = (0.3),
  )
  Batu_123   = duplicate (
    Batu_001,
      position = (42, 0, -83),
      scale = (0.3),
  )
  Batu_124   = duplicate (
    Batu_001,
      position = (42, 0, -79),
      scale = (0.3),
  )
  Batu_125   = duplicate (
    Batu_001,
      position = (42, 0, -53),
      scale = (0.3),
  )
  Batu_126   = duplicate (
    Batu_001,
      position = (46, 0, -77),
      scale = (0.3),
  )
  Batu_127   = duplicate (
    Batu_001,
      position = (46, 0, -53),
      scale = (0.3),
  )
  Batu_128   = duplicate (
    Batu_001,
      position = (47, 0, -23),
      scale = (0.3),
  )
  Batu_129   = duplicate (
    Batu_001,
      position = (49, 0, -31),
      scale = (0.3),
  )
  Batu_130   = duplicate (
    Batu_001,
      position = (48, 0, -35),
      scale = (0.3),
  )
  Batu_131   = duplicate (
    Batu_001,
      position = (48, 0, -43),
      scale = (0.3),
  )
  Batu_132   = duplicate (
    Batu_001,
      position = (53, 0, -17),
      scale = (0.3),
  )
  Batu_133   = duplicate (
    Batu_001,
      position = (51, 0, -31),
      scale = (0.3),
  )
  Batu_134   = duplicate (
    Batu_001,
      position = (50, 0, -35),
      scale = (0.3),
  )
  Batu_135   = duplicate (
    Batu_001,
      position = (52, 0, -79),
      scale = (0.3),
  )
  Batu_136   = duplicate (
    Batu_001,
      position = (52, 0, -77),
      scale = (0.3),
  )
  Batu_137   = duplicate (
    Batu_001,
      position = (52, 0, -49),
      scale = (0.3),
  )
  Batu_138   = duplicate (
    Batu_001,
      position = (58, 0, -37),
      scale = (0.3),
  )
  Batu_139   = duplicate (
    Batu_001,
      position = (58, 0, -41),
      scale = (0.3),
  )
  Batu_140   = duplicate (
    Batu_001,
      position = (58, 0, -85),
      scale = (0.3),
  )
  Batu_141   = duplicate (
    Batu_001,
      position = (61, 0, -17),
      scale = (0.3),
  )
  Batu_141   = duplicate (
    Batu_001,
      position = (61, 0, -37),
      scale = (0.3),
  )
  Batu_142   = duplicate (
    Batu_001,
      position = (61, 0, -41),
      scale = (0.3),
  )
  Batu_143   = duplicate (
    Batu_001,
      position = (61, 0, -49),
      scale = (0.3),
  )
  Batu_144   = duplicate (
    Batu_001,
      position = (61, 0, -53),
      scale = (0.3),
  )
  Batu_145   = duplicate (
    Batu_001,
      position = (61, 0, -85),
      scale = (0.3),
  )
  Batu_146   = duplicate (
    Batu_001,
      position = (67, 0, -23),
      scale = (0.3),
  )
  Batu_147   = duplicate (
    Batu_001,
      position = (67, 0, -31),
      scale = (0.3),
  )
  Batu_148   = duplicate (
    Batu_001,
      position = (68, 0, -35),
      scale = (0.3),
  )
  Batu_149   = duplicate (
    Batu_001,
      position = (68, 0, -43),
      scale = (0.3),
  )
  Batu_150   = duplicate (
    Batu_001,
      position = (68, 0, -47),
      scale = (0.3),
  )
  Batu_151   = duplicate (
    Batu_001,
      position = (68, 0, -55),
      scale = (0.3),
  )
  Batu_152   = duplicate (
    Batu_001,
      position = (68, 0, -61),
      scale = (0.3),
  )
  Batu_153   = duplicate (
    Batu_001,
      position = (67, 0, -65),
      scale = (0.3),
  )
  Batu_154   = duplicate (
    Batu_001,
      position = (67, 0, -73),
      scale = (0.3),
  )
  Batu_155   = duplicate (
    Batu_001,
      position = (68, 0, -77),
      scale = (0.3),
  )
  Batu_156   = duplicate (
    Batu_001,
      position = (74, 0, -85),
      scale = (0.3),
  )
  Batu_157   = duplicate (
    Batu_001,
      position = (74, 0, -71),
      scale = (0.3),
  )
  Batu_158   = duplicate (
    Batu_001,
      position = (74, 0, -67),
      scale = (0.3),
  )
  Batu_159   = duplicate (
    Batu_001,
      position = (74, 0, -29),
      scale = (0.3),
  )
  Batu_160   = duplicate (
    Batu_001,
      position = (74, 0, -25),
      scale = (0.3),
  )
  Batu_161   = duplicate (
    Batu_001,
      position = (74, 0, -17),
      scale = (0.3),
  )
  Batu_170   = duplicate (
    Batu_001,
      position = (27, 0, 85),
      scale = (0.3),
  )
  Batu_171   = duplicate (
    Batu_001,
      position = (27, 0, 68),
      scale = (0.3),
  )
  Batu_172   = duplicate (
    Batu_001,
      position = (27, 0, 64),
      scale = (0.3),
  )
  Batu_173   = duplicate (
    Batu_001,
      position = (20, 0, 83),
      scale = (0.3),
  )
  Batu_174   = duplicate (
    Batu_001,
      position = (21, 0, 80),
      scale = (0.3),
  )
  Batu_175   = duplicate (
    Batu_001,
      position = (21, 0, 57),
      scale = (0.3),
  )
  Batu_176   = duplicate (
    Batu_001,
      position = (20, 0, 54),
      scale = (0.3),
  )
  Batu_177   = duplicate (
    Batu_001,
      position = (21, 0, 33),
      scale = (0.3),
  )
  Batu_178   = duplicate (
    Batu_001,
      position = (17, 0, 38),
      scale = (0.3),
  )
  Batu_179   = duplicate (
    Batu_001,
      position = (18, 0, 85),
      scale = (0.3),
  )
  Batu_180   = duplicate (
    Batu_001,
      position = (16, 0, 75),
      scale = (0.3),
  )
  Batu_181   = duplicate (
    Batu_001,
      position = (16, 0, 65),
      scale = (0.3),
  )
  Batu_182   = duplicate (
    Batu_001,
      position = (11, 0, 33),
      scale = (0.3),
  )
  Batu_183   = duplicate (
    Batu_001,
      position = (11, 0, 69),
      scale = (0.3),
  )
  Batu_184   = duplicate (
    Batu_001,
      position = (12, 0, 80),
      scale = (0.3),
  )
  Batu_185   = duplicate (
    Batu_001,
      position = (11, 0, 83),
      scale = (0.3),
  )
  Batu_186   = duplicate (
    Batu_001,
      position = (8, 0, 83),
      scale = (0.3),
  )
  Batu_187   = duplicate (
    Batu_001,
      position = (8, 0, 75),
      scale = (0.3),
  )
  Batu_188   = duplicate (
    Batu_001,
      position = (8, 0, 59),
      scale = (0.3),
  )
  Batu_189   = duplicate (
    Batu_001,
      position = (8, 0, 33),
      scale = (0.3),
  )
  Batu_190   = duplicate (
    Batu_001,
      position = (6, 0, 62),
      scale = (0.3),
  )
  Batu_191   = duplicate (
    Batu_001,
      position = (1, 0, 78),
      scale = (0.3),
  )
  Batu_192   = duplicate (
    Batu_001,
      position = (1, 0, 57),
      scale = (0.3),
  )
  Batu_193   = duplicate (
    Batu_001,
      position = (3, 0, 54),
      scale = (0.3),
  )
  Batu_194   = duplicate (
    Batu_001,
      position = (-2, 0, 68),
      scale = (0.3),
  )
  Batu_195   = duplicate (
    Batu_001,
      position = (-2, 0, 62),
      scale = (0.3),
  )
  Batu_196   = duplicate (
    Batu_001,
      position = (-2, 0, 59),
      scale = (0.3),
  )
  Batu_197   = duplicate (
    Batu_001,
      position = (-2, 0, 38),
      scale = (0.3),
  )
  Batu_198   = duplicate (
    Batu_001,
      position = (-4, 0, 54),
      scale = (0.3),
  )
  Batu_199   = duplicate (
    Batu_001,
      position = (-7, 0, 80),
      scale = (0.3),
  )
  Batu_200   = duplicate (
    Batu_001,
      position = (-7, 0, 73),
      scale = (0.3),
  )
  Batu_201   = duplicate (
    Batu_001,
      position = (-7, 0, 54),
      scale = (0.3),
  )
  Batu_202   = duplicate (
    Batu_001,
      position = (-9, 0, 38),
      scale = (0.3),
  )
  Batu_203   = duplicate (
    Batu_001,
      position = (-9, 0, 57),
      scale = (0.3),
  )
  Batu_204   = duplicate (
    Batu_001,
      position = (-9, 0, 85),
      scale = (0.3),
  )
  Batu_205   = duplicate (
    Batu_001,
      position = (-12, 0, 83),
      scale = (0.3),
  )
  Batu_206   = duplicate (
    Batu_001,
      position = (-12, 0, 59),
      scale = (0.3),
  )
  Batu_207   = duplicate (
    Batu_001,
      position = (-12, 0, 38),
      scale = (0.3),
  )
  Batu_208   = duplicate (
    Batu_001,
      position = (-14, 0, 54),
      scale = (0.3),
  )
  Batu_209   = duplicate (
    Batu_001,
      position = (-14, 0, 75),
      scale = (0.3),
  )
  Batu_210   = duplicate (
    Batu_001,
      position = (-17, 0, 67),
      scale = (0.3),
  )
  Batu_211   = duplicate (
    Batu_001,
      position = (-17, 0, 40),
      scale = (0.3),
  )
  Batu_212   = duplicate (
    Batu_001,
      position = (-19, 0, 33),
      scale = (0.3),
  )
  Batu_213   = duplicate (
    Batu_001,
      position = (-19, 0, 43),
      scale = (0.3),
  )
  Batu_214   = duplicate (
    Batu_001,
      position = (-19, 0, 80),
      scale = (0.3),
  )
  Batu_215   = duplicate (
    Batu_001,
      position = (-24, 0, 85),
      scale = (0.3),
  )
  Batu_216   = duplicate (
    Batu_001,
      position = (-24, 0, 67),
      scale = (0.3),
  )
  Batu_217   = duplicate (
    Batu_001,
      position = (-24, 0, 64),
      scale = (0.3),
  )
  Batu_218   = duplicate (
    Batu_001,
      position = (-24, 0, 57),
      scale = (0.3),
  )
  Batu_219   = duplicate (
    Batu_001,
      position = (-22, 0, 54),
      scale = (0.3),
  )
  Batu_220   = duplicate (
    Batu_001,
      position = (-24, 0, 38),
      scale = (0.3),
  )
  Batu_221   = duplicate (
    Batu_001,
      position = (-22, 0, 34),
      scale = (0.3),
  )
  Batu_222   = duplicate (
    Batu_001,
      position = (-27, 0, 83),
      scale = (0.3),
  )
  Batu_223   = duplicate (
    Batu_001,
      position = (-29, 0, 80),
      scale = (0.3),
  )
  Batu_224   = duplicate (
    Batu_001,
      position = (-27, 0, 75),
      scale = (0.3),
  )
  Batu_225   = duplicate (
    Batu_001,
      position = (-32, 0, 78),
      scale = (0.3),
  )
  Batu_226   = duplicate (
    Batu_001,
      position = (-34, 0, 75),
      scale = (0.3),
  )
  Batu_227   = duplicate (
    Batu_001,
      position = (-32, 0, 57),
      scale = (0.3),
  )
  Batu_228   = duplicate (
    Batu_001,
      position = (-33, 0, 54),
      scale = (0.3),
  )
  Batu_229   = duplicate (
    Batu_001,
      position = (-37, 0, 62),
      scale = (0.3),
  )
  Batu_230   = duplicate (
    Batu_001,
      position = (-38, 0, 54),
      scale = (0.3),
  )
  Batu_231   = duplicate (
    Batu_001,
      position = (-43, 0, 54),
      scale = (0.3),
  )
  Batu_232   = duplicate (
    Batu_001,
      position = (-39, 0, 80),
      scale = (0.3),
  )
  Batu_233   = duplicate (
    Batu_001,
      position = (-44, 0, 38),
      scale = (0.3),
  )
  Batu_234   = duplicate (
    Batu_001,
      position = (-44, 0, 57),
      scale = (0.3),
  )
  Batu_235   = duplicate (
    Batu_001,
      position = (-44, 0, 85),
      scale = (0.3),
  )
  Batu_236   = duplicate (
    Batu_001,
      position = (-47, 0, 85),
      scale = (0.3),
  )
  Batu_237   = duplicate (
    Batu_001,
      position = (-47, 0, 78),
      scale = (0.3),
  )
  Batu_238   = duplicate (
    Batu_001,
      position = (-47, 0, 74),
      scale = (0.3),
  )
  Batu_239   = duplicate (
    Batu_001,
      position = (-47, 0, 57),
      scale = (0.3),
  )
  Batu_240   = duplicate (
    Batu_001,
      position = (-47, 0, 54),
      scale = (0.3),
  )
  Batu_241   = duplicate (
    Batu_001,
      position = (-49, 0, 33),
      scale = (0.3),
  )
  Batu_242   = duplicate (
    Batu_001,
      position = (-52, 0, 33),
      scale = (0.3),
  )
  Batu_243   = duplicate (
    Batu_001,
      position = (-54, 0, 73),
      scale = (0.3),
  )
  Batu_244   = duplicate (
    Batu_001,
      position = (-54, 0, 70),
      scale = (0.3),
  )
  Batu_245   = duplicate (
    Batu_001,
      position = (-54, 0, 57),
      scale = (0.3),
  )
  Batu_246   = duplicate (
    Batu_001,
      position = (-54, 0, 54),
      scale = (0.3),
  )
  Batu_247   = duplicate (
    Batu_001,
      position = (-59, 0, 83),
      scale = (0.3),
  )
  Batu_248   = duplicate (
    Batu_001,
      position = (-59, 0, 80),
      scale = (0.3)
  )
  Batu_249   = duplicate (
    Batu_001,
      position = (-59, 0, 38),
      scale = (0.3)
  )
  Batu_250   = duplicate (
    Batu_001,
      position = (-59, 0, 35),
      scale = (0.3)
  )

  # #Labirin tengah
  # for i in range (1,9):
  #     tree_rand1 = randint(-45, 30)
  #     tree_rand2 = randint(0, 0)
  #     tree_rand3 = randint(-30, 30)
  #     tree_01 = Entity(model = 'assets/Tree/Sakura 2.0.glb',
  #         scale = (1),
  #         position = (tree_rand1, tree_rand2, tree_rand3),
  #         )

  # #Labirin Bawah
  # for i in range (1,9):
  #     tree_rand4 = randint(-53, 75)
  #     tree_rand5 = randint(0, 0)
  #     tree_rand6 = randint(-85, -30)
  #     tree_01 = Entity(model = 'assets/Tree/Sakura 2.0.glb',
  #         scale = (1),
  #         position = (tree_rand4, tree_rand5, tree_rand6),
  #         )

  # #Labirin atas
  # for i in range (10):
  #     tree_rand7 = randint(-60, 22)
  #     tree_rand8 = randint(0, 0)
  #     tree_rand9 = randint(33, 85)
  #     tree_01 = Entity(model = 'assets/Tree/Sakura 2.0.glb',
  #         scale = (1),
  #         position = (tree_rand7, tree_rand8, tree_rand9),
  #         )
