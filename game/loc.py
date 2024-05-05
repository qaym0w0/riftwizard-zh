tags = {
    "physical": "物理",
    "fire": "火焰",
    "lightning": "闪电",
    "dark": "黑暗",
    "poison": "毒素",
    "holy": "神圣",
    "arcane": "奥术",
    "ice": "寒冰",
    "nature": "自然",
    "sorcery": "咒术",
    "conjuration": "召唤",
    "enchantment": "附魔",
    "word": "真言",
    "orb": "法球",
    "dragon": "龙",
    "translocation": "移形",
    "undead": "死灵",
    "elemental": "元素",
    "heal": "治疗",
    "acid": "酸化",
    "demon": "恶魔",
    "spider": "蜘蛛",
    "living": "活物",
    "construct": "构装体",
    "metallic": "金属",
    "eye": "眼",
    "glass": "玻璃",
    "chaos": "混沌",
    "blood": "鲜血",
    "tongue": "tongue", # ？
    "slime": "史莱姆",
    "shield": "护盾",
	# 下面的都没见过
    "buff_apply": "buff_apply",
    "debuff_apply": "debuff_apply",
    "shield_apply": "shield_apply",
    "shield_expire": "shield_expire",
    "sound_effect": "sound_effect",
    "leap": "leap",
    "arrow": "arrow",
    "petrification": "petrification",
    "glassification": "glassification",
    "immolate": "immolate",
    "thunderstrike": "thunderstrike",
    "armageddonblade": "armageddonblade",
    # 上面的都没见过
    "damage": "伤害",
    "range": "范围",
    "minion_health": "随从生命",
    "minion_damage": "随从伤害",
    "breath_damage": "吐息伤害",
    "minion_duration": "随从持续时间",
    "minion_range": "随从攻击范围",
    "duration": "持续时间",
    "max_charges": "最大充能",
    "radius": "半径",
    "num_summons": "召唤数量",
    "num_targets": "目标数量",
    "shields": "护盾",
    "shot_cooldown": "shot_cooldown", # TODO
    "strikechance": "打击概率",
    "cooldown": "冷却时间",
    "cascade_range": "弹射范围",
    "petrify": "石化",
    "petrified": "石化",
    "petrifies": "石化",
    "glassify": "玻璃化",
    "glassified": "玻璃化",
    "frozen": "冻结",
    "freezes": "冻结",
    "freeze": "冻结",
    "stunned": "眩晕",
    "stun": "眩晕",
    "stuns": "眩晕",
    "berserk": "狂暴",
    "poisoned": "中毒",
    "blind": "致盲",
    "blinded": "致盲",
    "quick_cast": "快速施放", # 没见过
}

schools = {}
for school in ["Fire", "Ice", "Lightning", "Nature", "Dark", "Holy", "Arcane", "Sorcery", "Conjuration", "Enchantment",]:
    schools[school] = tags[school.lower()]

damage_tags = {}
for type in ["Physical", "Fire", "Lightning", "Dark", "Poison", "Holy", "Arcane", "Ice",]:
    damage_tags[type] = tags[type.lower()]

tags_format = {
    # damage type
    "physical": "%s 点物理伤害",
    "fire": "%s 点火焰伤害",
    "lightning": "%s 点闪电伤害",
    "dark": "%s 点黑暗伤害",
    "poison": "%s 点毒素伤害",
    "holy": "%s 点神圣伤害",
    "arcane": "%s 点奥术伤害",
    "ice": "%s 点寒冰伤害",

    # upgrade attributes
    "damage": "%s 点伤害",
    "range": "%s 格",
    "minion_health": "%s 点生命",
    "minion_damage": "%s 点伤害",
    "breath_damage": "%s 点吐息伤害",
    "minion_duration": "%s 回合",
    "minion_range": "%s 格",
    "duration": "%s 个回合",
    "max_charges": "%s 点最大充能",
    "radius": "半径 %s 格",
    "num_summons": "%s 个",
    "num_targets": "%s 个",
    "shields": "%s 点护盾",
    "shot_cooldown": "%s 回合",
    "strikechance": "%s% 概率",
    "cooldown": "%s 回合",
    "cascade_range": "%s 格弹射范围",

    # other
    "heal": "%s 点生命",
}

clauses = {
    "channel": "这个法术至多可以引导 %s，引导持续的每个回合都会重复相同的效果",
}

spells = {
    "Death Bolt": "死亡之箭", # 这玩意明显是 neta 魔兽争霸里的黑暗之箭，但是那个是 black arrow
    "Fireball": "火球术",
    "Icicle": "冰锥",
    "Lifedrain": "生命吸取",
    "Lightning Bolt": "闪电箭",
    "Magic Missile": "魔法飞弹",
    "Poison Sting": "毒刺",
    "Wolf": "召唤狼",
    "Annihilate": "湮灭",
    "Boiling Blood": "沸腾之血", # 其实倾向于避免用“之”，沸腾血液有什么不好的吗
    "Bone Spear": "骨矛",
    "Chaos Barrage": "混沌箭雨",
    "Devour Mind": "吞噬心灵",
    "Disperse": "驱散",
    "Dreamwalk": "白日梦行",
    "Eye of Fire": "火焰之眼",
    "Eye of Ice": "寒冰之眼",
    "Eye of Lightning": "闪电之眼",
    "Eye of Rage": "狂怒之眼",
    "Fan of Flames": "火焰扇", # 黑暗之魂3
    "Freeze": "冰冻",
    "Goatia Offering": "邪羊献祭",
    "Healing Light": "治愈之光",
    "Heavenly Blast": "天堂爆破",
    "Hungry Maw": "饥饿嗜魔", # dnd
    "Iceball": "冰球",
    "Immolate": "燔祭",
    "Invoke Savagery": "唤起野性",
    "Magnetize": "磁化",
    "Melt": "熔化",
    "Mercurize": "汞化",
    "Moon Glaive": "月刃",
    "Petrify": "石化",
    "Plague of Undeath": "亡灵瘟疫", #亡灵天灾（（
    "Pyrostatic Pulse": "电焰脉冲",
    "Regeneration Aura": "再生光环",
    "Scourge": "天罚",
    "Soul Swap": "灵魂换位",
    "Thunder Strike": "雷霆打击",
    "Touch of Death": "死亡之触",
    "Toxic Spores": "有毒孢子",
    "Toxin Burst": "毒素爆发",
    "Aether Swap": "以太换位",
    "Arcane Orb": "奥术法球",
    "Basilisk Armor": "石化护甲",
    "Blazerip": "炽裂术",
    "Blinding Light": "眩目之光",
    "Blink": "闪现术",
    "Bloodshift": "鲜血转移",
    "Chain Lightning": "连锁闪电",
    "Choir of Angels": "天使唱诗班",
    "Darkness": "黑暗术", # dnd二环塑能
    "Death Chill": "致死严寒",
    "Devour Flesh": "吞噬血肉",
    "Dominate": "支配",
    "Earthen Sentinel": "大地哨兵",
    "Earthquake": "地震",
    "Flame Gate": "火焰之门", # 寒冰之墙
    "Frostfire Hydra": "霜火九头蛇", # 作为海德拉你不能移动是正常的吗？
    "Ghostball": "鬼球术",
    "Giant Bear": "召唤巨熊",
    "Glass Orb": "玻璃法球",
    "Holy Armor": "神圣护甲",
    "Holy Fire": "圣火",
    "Ironize": "铸铁身躯", # 太难听了
    "Lightning Halo": "闪电光圈", # 唉，被砍成圆环的技能
    "Lightning Spire": "闪电尖塔",
    "Lumbriogenesis": "蠕虫孳生",
    "Mystic Power": "神秘力量",
    "Mystic Vision": "神秘视野",
    "Nightmare Aura": "梦魇光环",
    "Plague of Filth": "污秽瘟疫",
    "Prison of Thorns": "荆棘囚笼",
    "Psychic Seedling": "灵能幼苗",
    "Seal Fate": "命定之死",
    "Shrapnel Blast": "破片迸发",
    "Sight of Blood": "血腥视线",
    "Silver Spear": "银色标枪",
    "Suspend Mortality": "死亡拒止",
    "Underworld Passage": "冥界通道",
    "Armageddon Blade": "审判之刃",
    "Blizzard": "暴风雪",
    "Blood Golem": "鲜血魔像",
    "Bone Barrage": "骸骨箭雨",
    "Burning Idol": "焚烬造像",
    "Call Seraph": "呼唤炽天使",
    "Carnival of Pain": "痛楚祭典",
    "Combust Poison": "毒素燃爆",
    "Conductance": "导体化",
    "Death Cleave": "死亡分裂",
    "Dispersion Field": "驱散立场",
    "Drain Pulse": "汲魂脉冲",
    "Essence Flux": "要素异变",
    "Fiery Tormentor": "炽火狱吏", # 拷问者？行刑者？这个的图像很自然让我想到魂3的狱卒和火刑魔女，拿着一个烙铁，这个形象来源于哪里呢
    "Fire Drake": "火焰巨龙",
    "Flame Burst": "炎爆术",
    "Floating Eye": "召唤浮眼",
    "Ice Drake": "冰霜巨龙",
    "Ice Orb": "冰霜法球",
    "Ice Vortex": "寒冰漩涡",
    "Imp Swarm": "小鬼集结",
    "Lightning Form": "闪电形态",
    "Lightning Storm": "闪电风暴",
    "Mass Calcification": "群体钙化",
    "Orb Control": "法球控制",
    "Pain Mirror": "痛苦之镜",
    "Permanence": "法术持久",
    "Petrification Aura": "石化光环",
    "Purity": "净化",
    "Pyrostatic Curse": "电焰诅咒",
    "Searing Seal": "灼热印记",
    "Siege Golems": "攻城魔像",
    "Siphon Shields": "虹吸护盾",
    "Stampede Form": "象群形态",
    "Storm Burst": "风暴爆发",
    "Storm Drake": "风暴巨龙",
    "The Restless Dead": "不息死者",
    "Vampiric Gaze": "吸血凝视",
    "Void Beam": "虚空射线",
    "Void Drake": "虚空巨龙",
    "Wall of Ice": "寒冰之墙",
    "Volcanic Eruption": "火山爆发",
    "Watcher Form": "监视者形态",
    "Wheel of Death": "死亡轮盘",
    "Ball Lightning": "球状闪电",
    "Bloodflame": "血焰术", # 难听
    "Blue Lion": "蓝狮子",
    "Call Archon": "呼唤执政官",
    "Cantrip Cascade": "小招倾泻",
    "Chill Wind": "凛冽寒风",
    "Death Shock": "死亡电击",
    "Fae Court": "仙灵庭院",
    "Flesh Fiend": "血肉恶魔",
    "Golden Skull": "金色颅骨",
    "Heavenly Idol": "天堂造像",
    "Ice Phoenix": "寒冰凤凰",
    "Mega Annihilate": "究极湮灭",
    "Night Hag": "老鬼婆", # DND
    "Pillar of Fire": "火焰之柱",
    "Ring of Spiders": "蜘蛛之环",
    "Slime Form": "史莱姆形态",
    "Soul Tax": "灵魂税",
    "Spider Queen": "蜘蛛女皇",
    "Teleport": "传送",
    "Arc Lightning": "弧形闪电",
    "Dragon Roar": "龙吼",
    "Faehaunt Garden": "蝴蝶花园", # 没法直译
    "Flock of Eagles": "召唤鹰群",
    "Furnace of Sorcery": "咒术熔炉",
    "Gold Drake": "黄金巨龙",
    "Heaven's Wrath": "天堂之怒",
    "Knightly Oath": "骑士誓言",
    "Mystic Memory": "神秘记忆",
    "Searing Orb": "灼热法球",
    "Twilight Gaze": "暮光凝视",
    "Hatebolts": "恶业之箭",
    "Multicast": "多重施法",
    "Soul Wind": "灵魂之风",
    "Spikeball Factory": "钉球工厂",
    "Word of Beauty": "美丽真言",
    "Word of Chaos": "混沌真言",
    "Word of Ice": "冰霜真言",
    "Word of Madness": "疯狂真言",
    "Word of Undeath": "不死真言", # 亡灵真言？
    "Wyrm Eggs": "游龙蛋",
    "Gates of Helheim": "赫尔海姆之门", # 所以 Aelf 到底是什么生物
    "Horde of Halfmen": "半人部族",
    "Rain of Fire": "陨石雨",
    "Ritual of Revelation": "启示仪式",
    "Summon Wizard": "召唤巫师",
}

skills = {
    "Arcane Accounting": "奥术节能",
    "Arcane Combustion": "奥术爆燃",
    "Arcane Shield": "奥术护盾",
    "Bone Guard": "骸骨卫士",
    "Chaos Familiar": "混乱仆从",
    "Conjured Aggression": "造物强袭",
    "Conjured Vitality": "造物活力",
    "Crystal Power": "水晶之力",
    "Deathchill Familiar": "死寒仆从",
    "Faestone": "仙灵石",
    "Frostbite": "霜咬", # 图里有张嘴
    "Frozen Fragility": "低温脆化",
    "Glittering Dance": "闪光之舞",
    "Hibernation": "冬眠",
    "Holy Water": "圣水",
    "Houndlord": "猎犬领主",
    "Hungry Dead": "饥饿死者",
    "Lifespark Lantern": "生灵弧灯",
    "Lightning Warp": "闪电跃迁",
    "Master of Memories": "记忆大师",
    "Megavenom": "剧毒",
    "Melting Armor": "熔化护甲",
    "Minion Regeneration": "随从再生",
    "Natural Healing": "自然回复",
    "Natural Vigour": "自然护身", # TODO
    "Paralyzing Venom": "麻痹毒液",
    "Prince of Ruin": "毁灭王子",
    "Radiant Chill": "寒气逼人",
    "Shielded Minions": "盾护随从",
    "Silkshifter": "蛛网行者",
    "Spell Sniper": "法术狙击",
    "Spider Spawning": "蜘蛛孳生",
    "Stormbrood Tricksters": "风巢诡魔", # 召唤出来的巨魔会闪现术
    "Toadblood Transmutation": "蟾血嬗变",
    "Unholy Alliance": "不洁同盟",
    "Venom Spit": "毒液喷射",
    "Voidflame Lantern": "虚空燃灯",
    "Acid Fumes": "酸雾",
    "Armorer": "甲胄幻形", # TODO
    "Blood Anima": "鲜血灵体",
    "Blood Reaping": "鲜血收割",
    "Chaos Casting": "混沌施法",
    "Collected Agony": "苦痛积聚",
    "Demonic Cruelty": "恶魔心肠", # 这个真的好难听 TODO
    "Earthwrath": "大地之怒",
    "Fae Malevolence": "邪灵作祟", # TODO
    "Fiery Judgement": "火焰审判",
    "Ghostfire": "鬼火",
    "Hemocorruption": "血液污染", # 因为只是有毒所以感觉还是污染好一点
    "Holy Thunder": "神圣雷霆",
    "Hordemancer": "群体召唤", # TODO
    "Horror": "恐惧",
    "Hypocrisy": "伪善",
    "Master of Space": "空间大师",
    "Master of Time": "时间大师",
    "Multimancy": "多重施法",
    "Necrostatics": "亡灵起电", # TODO 想弄点弗兰肯斯坦进去
    "Purestrike": "纯洁打击",
    "Pyrophilia": "嗜火症",
    "Righteous March": "正义之师",
    "Scalefeather Egregore": "鳞羽群灵", # 鳞羽格式塔（？ 这个怪名字叫feathered serpent啊 就是羽蛇 （Egregore是群体意念聚集的灵体）
    "Searing Heat": "炎炎酷热",
    "Starfire": "星火交辉",
    "Thorn Garden": "荆棘花园",
    "Wordspeaker": "真言诵者", # 或者咏者？颂者？
    "Chastisement": "惩戒", # 这个图标和 Scourge 一样啊，那都叫惩戒行吗（不行
    "Cracklevoid": "虚空电鸣",
    "Echomancer": "法术回响",
    "Ice Tap": "共振冰棱", # 冰坠子
    "Icy Vengeance": "冰霜复仇",
    "Inferno Engines": "炼狱引擎",
    "Lightning Frenzy": "闪电狂热",
    "Moonspeaker": "月语者",
    "Scalespinner": "鳞甲变换",
    "Shatter Shards": "碎冰裂片",
    "Steam Anima": "蒸汽灵体",
    "Storm Caller": "呼唤风暴",
    "Arch Conjurer": "召唤大师",
    "Arch Enchanter": "附魔大师",
    "Arch Sorcerer": "咒术大师",
    "Blood Lord": "鲜血领主",
    "Chaos Poet": "混沌诗人",
    "Dark Lord": "黑暗领主",
    "Disintegrator": "法术解离", # 解离术士？解离单元？魔力解离？感觉解离器听起来像个有实体的工具
    "Enchanters Boon": "附魔幻形", # TODO
    "Dragon Lord": "巨龙领主",
    "Fire Lord": "火焰领主",
    "Ice Lord": "冰霜领主",
    "Light Lord": "光明领主",
    "Metal Lord": "金属领主",
    "Nature Lord": "自然领主",
    "Orb Lord": "法球领主",
    "Scent of Blood": "血腥嗅迹",
    "Serpents of Chaos": "混沌之蛇",
    "Shock Value": "震魂夺魄", # 敌人死于雷电伤害使视线内敌人狂暴
    "Soul Harvest": "灵魂收割",
    "Thunder Lord": "雷霆领主",
    "Translocation Master": "传送大师",
    "Unblinking Eye": "不瞬之目",
    "Void Lord": "虚空领主",
    "Void Spikes": "虚空棘刺",
}

upgrades = {
    "Soul Battery": "灵魂充能",
    "Winter Bolt": "凛冬箭",
    "Chaos Skeletons": "混沌骷髅",
    "Chaos Ball": "混沌球",
    "Ash Ball": "灰烬球",
    "Meteor": "火流星",
    "Freezing": "霜冻冰锥",
    "Ice Spear": "冰枪疾射",
    "Icicle Harvest": "冰锥回收",
    "Blood Bond": "生命纽带",
    "Life Funnel": "生命漏斗",
    "Blindcasting": "无需视线",
    "Channeling": "引导施法",
    "Electric Ink": "电能复写",
    "Energy Bolt": "能量箭",
    "Shield Burn": "护盾烧却",
    "Disruption Bolt": "干扰飞弹",
    "Arcane Crossfire": "奥术交火",
    "Ricochet": "弹射飞弹",
    "Acidity": "剧毒入髓",
    "Silk Shot": "蛛丝射击",
    "Stinger Barrage": "毒素爆发",
    "Wolf Pack": "群狼术",
    "Ice Hound": "寒冰猎犬",
    "Clay Hound": "黏土猎犬",
    "Cascade": "倾泻湮灭",
    "Comprehensive Annihilation": "全面湮灭",
    "Doom Storm": "毁灭风暴",
    "Extra Damage": "额外伤害",
    "Duration": "持续回合",
    "Holy Fury": "神圣怒火",
    "Dark Fury": "黑暗怒火",
    "Infernal Spear": "炎狱咒祝",
    "Toxic Spear": "爆炸毒枪",
    "Stun Spear": "Stun Spear",
    "Mega Barrage": "超级弹幕",
    "Shockwaves": "冲击波",
    "Smart Bolts": "智能射弹",
    "Huskification": "尸壳化",
    "Spirit Eater": "吞噬灵体",
    "Gluttony": "暴食",
    "Violent Warp": "暴力跃迁",
    "Protective Warp": "防护跃迁",
    "Eye of Fireballs": "火球之眼",
    "Fiery Onlooker": "火焰观者",
    "Eye of Conflaguration": "燎原之眼",
    "Frosty Onlooker": "寒霜观者",
    "Eye of Freezing": "冻寒之眼",
    "Eye of Iceballs": "冰球之眼",
    "Archon Eye": "执政官之眼",
    "Eye of Thunderstrike": "雷击之眼",
    "Penetrating Gaze": "穿透凝视",
    "Lycanthropy": "狼人疫病",
    "Infectious Rage": "集群感染",
    "Burning Rage": "怒火中烧",
    "Healing Hearthfire": "治愈之炎",
    "Fan of Frostfire": "霜火技艺",
    "Wildfire": "野火燎原",
    "Refreezing": "再度冻结",
    "Mass Freeze": "集群冻结",
    "Quickcast": "快速施法",
    "Reincarnation": "转世轮回",
    "Pain Aura": "痛苦光环",
    "Maggot Host": "蛆群主脑",
    "Shielding Light": "护卫之光",
    "Purifying Light": "净化之光",
    "Heartflame": "心灵之火",
    "Spirit Bind": "圣罚魂缚",
    "Shield": "护盾",
    "Echo Heal": "圣愈共鸣",
    "Gnashing Teeth": "磨牙凿齿",
    "Invincible Maw": "无敌巨口",
    "Void Maw": "虚空亚种",
    "Cloud Combustion": "风暴借势",
    "Ice Crush": "冰屑破片",
    "Fae Ball": "敲冰戛玉",
    "Conflaguration": "连锁焚烧",
    "Radiant Heat": "焚灭扩散",
    "Dragon Soul": "龙魂觉醒",
    "Venomous Bite": "剧毒撕咬",
    "Savage Leap": "野蛮跃击",
    "Scavengers": "狼群之道",
    "Radioactivity": "放射污染",
    "Electromagnetism": "磁场放电",
    "Liquid Magnetism": "流性磁导",
    "Mass Melt": "群体熔化",
    "Ice Penetration": "熔透寒冰",
    "White Flame": "白色火焰",
    "Morbidity": "恶毒金属",
    "Corrosion": "熔蚀护甲",
    "Toxic Fumes": "毒瘴污染",
    "Mercurial Vengeance": "活化感染",
    "Glimmerblade": "光辉剑刃",
    "Electroblade": "雷电赋能",
    "Steelshaping": "金属共鸣",
    "Glassify": "玻璃化",
    "Arcane Conductivity": "奥术传导",
    "Rocky Servitude": "岩石奴役",
    "Max Health Loss": "最大生命损伤",
    "Fire Vulnerability": "火焰脆弱",
    "Plague of Undead": "亡者疫灾",
    "Chaos Pulse": "混沌脉冲",
    "Lesser Cascade": "低联散射",
    "Greater Cascade": "超联迸射",
    "Heal": "治疗量",
    "Global": "全图治疗",
    "Redemption": "天理昭彰",
    "Conversion": "支配戮民",
    "Mass Scourge": "族群天罚",
    "Forced Transfer": "强制转换",
    "Max Charges": "充能上限",
    "Storm Power": "风暴蓄能",
    "Heaven Strike": "天堂雷击",
    "Flametouch": "火焰之触",
    "Touch of the Vampire": "吸血之触",
    "Touch of the Reaper": "死神之触",
    "Hand of Death": "死亡之手",
    "Num Summons": "召唤数量",
    "Grey Mushbooms": "瘫痪菌株",
    "Red Mushbooms": "爆燃变异",
    "Glass Mushbooms": "玻璃菌株",
    "Herbal Remedy": "草药制备",
    "Withertoxin": "邪恶巫毒",
    "Toxin Bomber": "毒素炸弹",
    "Petrification": "石化光线",
    "Blazerip Orb": "炽裂法球",
    "Double Shot": "双重射击",
    "Orb Detonation": "法球激发",
    "Dual Blazerip": "双向爆闪",
    "Aether Poison": "以太之毒",
    "Blazebugs": "焱虫增殖",
    "Halting Light": "顿滞神光",
    "Searing Light": "烈焰神光",
    "Dissolution": "分散闪现",
    "Thunderblink": "雷霆闪现",
    "Radius": "半径",
    "Damage": "伤害",
    "Range": "射程",
    "Toxic Shift": "Toxic Shift",
    "Chain Fireball": "连锁火球",
    "Cloud Conductance": "云层导电",
    "Lightning Shield": "闪电护盾",
    "Dual Angels": "战斗天使",
    "Mercy": "圣光感化",
    "Massive Chorus": "天堂诗班",
    "Darkvision": "黑暗视觉",
    "Dark Clouds": "暗之死云",
    "Eternal Darkness": "永恒之暗",
    "Icy Necromancy": "亡灵冰术",
    "Slaughter Chill": "巫毒寒战",
    "Mass Death Chill": "灭绝寒潮",
    "Controlled Appetite": "节制吞噬",
    "Mass Feeding": "分摊治愈",
    "Charred Flesh": "焦焚仆役",
    "HP Threshold": "血量阈值",
    "Brute Force": "蛮力",
    "Undead Servitude": "不死奴役",
    "Earthquake Totem": "地震图腾",
    "Stinging Totem": "毒刺图腾",
    "Holy Totem": "神圣图腾",
    "Safety": "自然庇佑",
    "Aftershocks": "余波未尽",
    "Magnitude 8.0": "天震地骇",
    "Burst Fire": "火焰爆发",
    "Eye Gate": "火瞳之门",
    "Starfire Gate": "星火之门",
    "Crystal Eyes Hydra": "晶眼亚种",
    "Freezing Ice": "急冻霜火",
    "Hydra Reclamation": "前仆后继",
    "Ghost King": "游魂之王",
    "Ghost Mass": "百鬼夜行",
    "Metal Bear": "金属巨熊",
    "Venom Bear": "毒液巨熊",
    "Blood Bear": "鲜血巨熊",
    "Petrification Orb": "石化法球",
    "Orb Shards": "破碎迸射",
    "Enchantment Refraction": "魔力折射",
    "Greater Armor": "改良装甲",
    "Crystal Armor": "铸晶装甲",
    "Smiting Thorns": "荆棘护佑",
    "Holy Smite": "神怒一击",
    "Divine Blaze": "神性炽裂",
    "Heaven Call": "天堂号令",
    "Armor Plating": "装甲镀层",
    "Permanent Transmutation": "永续",
    "Arcane Insulation": "奥术绝缘",
    "Ring of Fire": "火焰之环",
    "Radioactive Field": "辐射场",
    "Lightning Nova": "闪电新星",
    "Mass Blasting": "集群迸射",
    "Wall Penetration": "墙体渗透",
    "Resistance Penetration": "抗性穿透",
    "Toxogenesis": "毒素生物",
    "Mechanogenesis": "机械造物",
    "Ectogenesis": "外质生物",
    "Damage Bonus": "伤害增益",
    "Intensity": "强度",
    "Bonus": "增益",
    "Vision Aura": "视野光环",
    "Dark Dream": "黑暗梦境",
    "Electric Dream": "电气梦境",
    "Fever Dream": "狂热梦境",
    "Minion Duration": "随从持续回合",
    "Serpent Plague": "枭蛇之灾",
    "Minion Damage": "随从伤害",
    "Minion Health": "随从生命",
    "Iron Prison": "钢铁囚笼",
    "Icy Prison": "寒冰囚笼",
    "Psychic Fields": "灵能域界",
    "Immortal Forest": "不朽瑶林",
    "Parasitic Growth": "槲寄生",
    "Spreading Curse": "散播诅咒",
    "Genocide": "灭绝术",
    "More Shrapnel": "改良破片",
    "Puncturing Blast": "穿刺爆破",
    "Magnetized Shards": "索敌破片",
    "Demon Frenzy": "恶魔狂热",
    "Copper Shaft": "青铜轴体",
    "Consecration": "银枪祝圣",
    "Endlessness": "绵延不绝",
    "Mass Immortaity": "不朽之族",
    "Twilight Essence": "暮光之子",
    "Tremorsensitivity": "震动感应",
    "Armor of Armageddon": "终末装甲",
    "Mass Armaments": "连锁湮灭",
    "Mega Armageddon": "最终决战",
    "Flash Freeze": "急冻风暴",
    "Hailstorm": "坠冰风暴",
    "Snow Feathers": "霜羽祝福",
    "Greater Thorns": "锋锐荆棘",
    "Vampire Golem": "血族造物",
    "Bone Spears": "贯通之枪",
    "Cursed Bones": "诅咒之骨",
    "Bone Explosion": "骸骨爆碎",
    "Archon Beam": "波形光束",
    "Moonblade": "月光铸剑",
    "Heal Aura": "治愈光环",
    "Holy Fire Aura": "圣焰光环",
    "Lifesteal": "生命窃取",
    "Death Power": "死亡巫能",
    "Torment": "无尽折磨",
    "Paralyzing Combustion": "瘫痪诱发",
    "Flame Rave": "烈火狂潮",
    "Toxic Embers": "剧毒余烬",
    "Multicopy": "多重拷贝",
    "Resistance Debuff": "抗性削弱",
    "Num Targets": "目标数量",
    "Felomancy": "咒猫呼唤",
    "Ursomancy": "血熊呼唤",
    "Frostfire Tormentor": "霜火刑罚",
    "Metallic Tormentor": "金属拷问",
    "Tormenting Mass": "集群召唤",
    "Broodlings": "幼体增殖",
    "Metal Dragon": "金属巨龙",
    "Dragon Mage": "巨龙法师",
    "Melting Flame": "熔融烈焰",
    "Bright Flame": "明亮烈焰",
    "Spreading Flame": "烈焰扩散",
    "Stone Gaze": "石化魔眼",
    "Eyemage": "拟态魔眼",
    "Regenerating Shields": "护盾再生",
    "Dracolich": "龙巫妖",
    "Frostgleam": "寒冻闪爆",
    "Faebound Orb": "冰精法球",
    "Blizzard Orb": "暴雪法球",
    "Metal Swarm": "金属魔潮",
    "Dark Swarm": "黑暗魔潮",
    "Endless Swarm": "无尽魔潮",
    "Lingering Form": "残影形态",
    "Fire Form": "火焰形态",
    "Crackling Aura": "电鸣光环",
    "Particle Storm": "粒子风暴",
    "Lightning Star": "闪电连星",
    "Spirit Harvest": "灵体收割",
    "Fae Bones": "仙化亡灵",
    "Burning Bones": "燃烧亡灵",
    "Bone Shards": "碎骨迸射",
    "Flesh Harvest": "血肉狂欢",
    "Dulled Pain": "痛感钝化",
    "Burning Pain": "蚀骨之火",
    "Crumbling Aura": "崩碎光环",
    "Wormification Aura": "岩蠕光环",
    "Resistance Melting": "外壳熔解",
    "Linear Conductance": "线性传导",
    "Pyrostatic Chaos": "混沌链接",
    "Slow Burn": "噬体之焰",
    "Chaos Seal": "元素混响",
    "Fire Harvest": "火焰收割",
    "Assistant Cannoneers": "炮兵小队",
    "Recycling": "战场回收",
    "Chaos Cannon": "混沌造物",
    "Shield Steal": "护盾窃取",
    "Fae Stampede": "仙灵祝福",
    "Burning Stampede": "燃烧巨象",
    "Metal Stampede": "金属践踏",
    "Stormshield": "风暴护盾",
    "Dual Nova": "双核新星",
    "Spirit Nova": "风暴共鸣",
    "Storm Summoning": "风暴召唤",
    "Ghost Drake": "幽灵巨龙",
    "Drake Swap": "巨龙换位",
    "Junk Golems": "废品傀儡",
    "Elemental Spirits": "元素篡夺",
    "Restless Minions": "无休战仆",
    "Toxic Gaze": "毒性凝视",
    "Vampiric Tax": "吸血税",
    "Refracting Gaze": "目光折射",
    "Void Binding": "虚空燔祭",
    "Star Beam": "星火射线",
    "Voidcurse": "虚空诅咒",
    "Shields": "护盾",
    "Essence Drake": "本源巨龙",
    "Flow Range": "喷发范围",
    "Wallcano": "墙体喷发",
    "Hungry Wall": "噬命之欲",
    "Fae Wall": "仙灵祝福",
    "Endless Wall": "无尽冰幕",
    "Pyrostatic Watcher Form": "电焰守卫",
    "Void Watcher Form": "虚空守卫",
    "Chain Watcher Form": "连锁守卫",
    "Cheat Fate": "瞒天过海",
    "Final Burst": "高压过载",
    "Drakebirth": "巨龙降生",
    "Pyrostatics": "升压爆燃",
    "Holy Bolt": "神圣之箭",
    "Shimmermane": "微光",
    "Burning Lion": "烈焰亚种",
    "Heal Beam": "愈合波动",
    "Beam Arc": "电弧集束",
    "Storm Archon": "冰暴军团",
    "Cantrip Burst": "定点爆破",
    "Orb Cascade": "法球共鸣",
    "Evocation Amalgamation": "巫术唤灵",
    "Ice Guardians": "冰灵加护",
    "Dual Wind": "双面驶风",
    "Arcane Storm": "奥术风暴",
    "Fire Shock": "火焰电击",
    "Corpse Construct": "尸体重组",
    "Winter Faery": "冬之精灵",
    "Summon Queen": "召唤女皇",
    "Glass Faery": "玻璃精灵",
    "Belly Flop": "Belly Flop",
    "Barbeque Fiends": "灼肉恶魔",
    "Worm Lord": "蠕虫领主",
    "Ghost Caller": "通灵仪式",
    "Bone Wheel": "死亡之轮",
    "Blood Skull": "骨山血海",
    "Fire Gaze": "烈焰之眼",
    "Shield Gaze": "修复之眼",
    "Bastion of Immortality": "不灭之壁",
    "Reincarnations": "转世轮回",
    "Ice Aura": "冰霜光环",
    "Dark Annihilation": "黑暗湮灭",
    "Arcane Annihilation": "奥术湮灭",
    "Spear Hag": "骨矛女巫",
    "Nightmare Hag": "夜魇女巫",
    "Bone Queen": "Bone Queen",
    "Disrupting Flames": "干扰烈焰",
    "Pillar of Annihilation": "湮灭之柱",
    "Turbo Toxin": "毒网",
    "Long Webs": "巨网",
    "Aether Spiders": "以太族群",
    "Fire Slime": "烈焰亚种",
    "Ice Slime": "霜寒亚种",
    "Void Slime": "虚空亚种",
    "Arcane Taxation": "奥术苛税",
    "Insta Tax": "瞬发协议",
    "Mass Taxation": "群体征收",
    "Aether Queen": "以太先驱",
    "Steel Queen": "钢之女皇",
    "Vampire Queen": "血族皇后",
    "Group Teleport": "群体传送",
    "Void Teleport": "虚空传送",
    "Proton Storm": "质子风暴",
    "Enervation": "精妙施法",
    "Multi Flash": "多重火花",
    "Draconic Vitality": "巨龙生机",
    "Draconic Vigor": "巨龙活力",
    "Draconic Majesty": "巨龙威严",
    "Guardian Gnomes": "侏儒守卫",
    "Fae Flies": "仙化飞蝇",
    "Glass Garden": "玻璃花园",
    "Army of Eagles": "猎鹰军团",
    "Shielded Eagles": "猎鹰甲胄",
    "Thunder Claw": "雷霆之爪",
    "Untouchable Majesty": "上兽之威",
    "Flames of Sorcery": "炉火升腾",
    "Imp Smithy": "青铜仲魔",
    "Arcane Eyebolts": "奥术猎犬",
    "Dragon Saint": "至圣之威",
    "Immortal Dragon": "金之不朽",
    "Culling": "抹除打击",
    "Halt Heretics": "打断邪术",
    "Fiery Wrath": "圣光烈焰",
    "Void Court": "虚空审判",
    "Storm Court": "暴风审判",
    "Chaos Court": "混沌审判",
    "Distant Memory": "久远回忆",
    "Deep Reflection": "深度回想",
    "Shield of Memories": "记忆护盾",
    "Explosive Orb": "爆炸过载",
    "Matter Melting": "无坚不熔",
    "Flame Rift": "火焰裂隙",
    "Arcane Gaze": "奥术凝视",
    "Boomerang": "回旋弩矢",
    "Toxic Hatred": "淬毒箭头",
    "Torment Harvest": "煎熬收割",
    "Copies": "Copies",
    "Ensoulment": "灵魂出窍",
    "Arcane Wind": "奥法之风",
    "Defense System": "自卫系统",
    "Manufactory": "集群装配",
    "Copper Spikeballs": "青铜铸法",
    "Beauty of Steel": "钢之美德",
    "Shield Strip": "护盾剥离",
    "Echoing Beauty": "美德回响",
    "Animated Chaos": "诱导降临",
    "Chaos Gifts": "混沌恩赐",
    "Echoing Chaos": "混沌回响",
    "Echoing Ice": "冰之回响",
    "Endless Ice": "共鸣冰语",
    "Word of Wind": "速咏成风",
    "Selective Madness": "精妙吟唱",
    "Echoing Madness": "妄语回响",
    "Guardians of Madness": "疯诞降临",
    "Hatred of Life": "亡者之憎",
    "Spirit Gift": "幽灵馈赠",
    "Spirit of Lichdom": "巫魂涌现",
    "Magic Eggs": "魔法胎教",
    "Radiant Eggs": "炫光龙蛋",
    "Scale Harvest": "Scale Harvest",
    "Aelf Horde": "Aelf Horde",
    "Fae Aelves": "Fae Aelves",
    "Elite Aelves": "Elite Aelves",
    "Trollblooded Halfmen": "巨魔亚种",
    "Metallic Halfmen": "全金属化",
    "Burning Halfmen": "烈焰血统",
    "Chaos Storm": "混沌风暴",
    "Rain of Dragons": "龙火技艺",
    "Pyrostatic Storm": "流星掣电",
    "Holy Horde": "Holy Horde",
    "Blasphemy": "亵渎仪式",
    "Arcane Revelation": "奥能绽放",
    "Clay Wizard": "黏土秘术",
    "Ghost Wizard": "幽灵巫师",
    "Wizard Gang": "战法小队",
}

consumables = {
    "Healing Potion": "治疗药水",
    "Mana Potion": "法力药水",
    "Teleporter": "传送器",
    "Golden Stopwatch": "金质怀表",
    "Chaos Bell": "混乱之铃",
    "Death Dice": "死亡骰子",
    "Portal Key": "传送钥匙",
    "Earthquake Orb": "地震法球",
    "Oculus": "天眼",
    "Aether Dagger": "以太匕首",
    "Bag of Spikes": "钉球袋",
    "Orb of Corruption": "腐化法球",
}

ring_tags = {
    "Fiery": "Fiery",
    "Icy": "Icy",
    "Electric": "Electric",
    "Living": "Living",
    "Sinister": "Sinister",
    "Golden": "Golden",
    "Mystic": "Mystic",
    "Sorcerous": "Sorcerous",
    "Enchanting": "Enchanting",
    "Conjured": "Conjured",
}

ring_stats = {
    "Dagger": "Dagger",
    "Orb": "Orb",
    "Tome": "Tome",
    "Lens": "Lens",
    "Flag": "Flag",
    "Disk": "Disk",
    "Scale": "Scale",
    "Claw": "Claw",
    "Fang": "Fang",
    "Hourglass": "Hourglass",
    "Horn": "Horn",
}

shrines = {
    "Ruby Heart": "Ruby Heart",
    "Exotic Pet Shop": "珍稀宠物商店",
    "Scroll of Spells": "法术卷轴",
    "Treasure Chest": "宝物箱",
    "Sigil Chest": "召唤法印箱", # TODO
    "Box of Wizard Caps": "巫师帽盒",
    "Hat Chest": "帽子箱",
    "Staff Chest": "法杖箱",
    "Shoe Box": "鞋盒",
    "Armor Chest": "盔甲箱",
    "Trinket Box": "饰品盒",
    "Scroll of Skills": "能力卷轴",
}
for k, v in ring_tags.items():
    name = "%s Trinket Chest" % k
    shrines[name] = "%s饰品箱" % v
for k, v in ring_stats.items():
    name = "%s Chest" % k
    shrines[name] = "%s箱" % v

equipments = {
    "The Bladestaff": "利刃法杖",
    "Geometer's Staff": "制图师法杖",
    "Memory Staff": "记忆法杖",
    "Banner of the Horde": "部族旗帜",
    "Storm Oculus": "Storm Oculus",
    "Void Oculus": "Void Oculus",
    "Pyrostatic Oculus": "Pyrostatic Oculus",
    "Twilight Oculus": "Twilight Oculus",
    "Crystal Oculus": "Crystal Oculus",
    "Purity Oculus": "Purity Oculus",
    "Arcane Amplifier": "Arcane Amplifier",
    "The Flamenweaver": "The Flamenweaver",
    "Treelord Staff": "Treelord Staff",
    "Aetherlord Staff": "Aetherlord Staff",
    "Filthlord Staff": "Filthlord Staff",
    "Flaming Claw Staff": "Flaming Claw Staff",
    "Icy Claw Staff": "Icy Claw Staff",
    "Scepter of Mischief": "Scepter of Mischief",
    "Drakenstaff": "Drakenstaff",
    "The Purifier": "The Purifier",
    "Silvermelt": "Silvermelt",
    "Sorcwinter": "Sorcwinter",
    "The Dynamo": "The Dynamo",
    "The Blazeloom": "The Blazeloom",
    "Starblesser": "Starblesser",
    "The Sparkloom": "The Sparkloom",
    "Wintersting": "Wintersting",
    "Red Majesty": "Red Majesty",
    "Blastmaker": "Blastmaker",
    "Embermaker": "Embermaker",
    "Mantismaker": "Mantismaker",
    "Sprigganmaker": "Sprigganmaker",
    "Impmaker": "Impmaker",
    "Crackledarkener": "Crackledarkener",
    "Scepter of Sorrows": "Scepter of Sorrows",
    "Glassy Fae Staff": "玻璃仙灵法杖",
    "Quill Staff": "Quill Staff",
    "Robe of Ice": "冰霜法袍",
    "Robe of Fire": "火焰法袍",
    "Robe of Void": "虚空法袍",
    "Robe of Storms": "风暴法袍",
    "Robe of the Druids": "德鲁伊法袍",
    "Fae Plate": "仙灵板甲",
    "Vampiric Vestments": "吸血背心",
    "Dwarven Chainmail": "矮人链甲",
    "Elven Chainmail": "精灵链甲", #？
    "Soulmail": "魂甲",
    "Basilisk Scale Armor": "石化鳞甲",
    "Earthtroll Armor": "大地巨魔铠甲",
    "Stormtroll Armor": "风暴巨魔铠甲",
    "Robe of Twilight": "暮光法袍",
    "Robe of Agony": "苦痛法袍",
    "Robe of Frostfire": "霜火法袍",
    "Robe of Crystals": "水晶法袍",
    "Marksman Cap": "射手帽",
    "Warlord Helm": "Warlord Helm", # TODO
    "Spirit Visor": "Spirit Visor",
    "Brain Hat": "头脑帽",
    "Cannibal Mask": "食人面具", # 怎么表达同类相食的感觉
    "Helm of the Host": "宿主头盔",
    "Icy Chill Mask": "Icy Chill Mask",
    "Stone Mask": "Stone Mask",
    "Eye Helm": "Eye Helm",
    "Fire Helm": "Fire Helm",
    "Ice Helm": "Ice Helm",
    "Lightning Helm": "Lightning Helm",
    "Dark Helm": "Dark Helm",
    "Nature Helm": "Nature Helm",
    "Holy Helm": "Holy Helm",
    "Arcane Helm": "Arcane Helm",
    "Metallic Helm": "Metallic Helm",
    "Fire Frenzy Mask": "Fire Frenzy Mask",
    "Ice Frenzy Mask": "Ice Frenzy Mask",
    "Arcane Frenzy Mask": "Arcane Frenzy Mask",
    "Summer Crown": "夏季皇冠",
    "Winter Crown": "冬季皇冠",
    "Spring Crown": "春季皇冠",
    "Autumn Crown": "秋季皇冠",
    "Bloodspike Crown": "Bloodspike Crown",
    "Earthmeld Boots": "Earthmeld Boots",
    "Travellers Shoes": "Travellers Shoes",
    "Cantrip Clogs": "Cantrip Clogs",
    "Timestriders": "Timestriders",
    "Drill Shoes": "Drill Shoes",
    "Winged Shoes": "Winged Shoes",
    "Silken Sandals": "Silken Sandals",
    "Snow Shoes": "Snow Shoes",
    "Translocation Boots": "Translocation Boots",
    "Gnome Shoes": "Gnome Shoes",
    "Slime Shoes": "Slime Shoes",
    "Kobold Clogs": "Kobold Clogs",
    "Ogre Boots": "Ogre Boots",
    "Ghost Slippers": "Ghost Slippers",
    "Storm Boots": "Storm Boots",
    "Exploding Boots": "Exploding Boots",
    "Finger 6": "Finger 6",
    "Ankh": "Ankh",
    "Drakentooth": "Drakentooth",
    "Eye Rock Pendant": "Eye Rock Pendant",
    "Amber Cube": "Amber Cube",
    "Skull Necklace": "Skull Necklace",
    "Red Obsidian Shard": "Red Obsidian Shard",
    "Jade Shard": "Jade Shard",
    "Reality Anchor": "Reality Anchor",
    "Amulet of Undeath": "Amulet of Undeath",
    "Vial of Ambrosia": "Vial of Ambrosia",
    "Amulet of Emerald Flame": "Amulet of Emerald Flame",
    "Monkey Skull Amulet": "Monkey Skull Amulet",
    "Blood Ruby": "Blood Ruby",
    "Bramblethorn": "Bramblethorn",
    "Toadthorn": "Toadthorn",
    "Devilthorn": "Devilthorn",
    "Witch Whistle": "Witch Whistle",
    "Snowy Fursphere": "Snowy Fursphere",
    "Living Emberstone": "Living Emberstone",
    "Silken Links": "Silken Links",
    "Winter Links": "Winter Links",
    "Wrath Links": "Wrath Links",
    "Jar of Trollblood": "巨魔血坛子",
    "Jar of Embers": "余烬坛子",
    "Jar of Quicksilver": "水银坛子",
    "Jar of Ectoplasm": "灵质坛子",
    "Poison Pipe": "毒素吹箭",
    "Time Pipe": "时光吹箭",
    "Ink Pipe": "墨汁吹箭",
    "Ice Pipe": "冰霜吹箭",
    "Purple Curse Doll": "紫色巫蛊",
    "Ugly Curse Doll": "丑陋巫蛊",
    "Red Curse Doll": "红色巫蛊",
}
for k, v in ring_tags.items():
    for k2, v2 in ring_stats.items():
        name = "%s %s" % (k, k2)
        equipments[name] = "%s %s" % (v, v2)
for k, v in schools.items():
    name = "%s Wand" % k
    equipments[name] = "%s魔杖" % v
for k,v in damage_tags.items():
    name = "%s Shield" % k
    equipments[name] = "%s护盾" % v

monsters = {
    "Goblin": "哥布林",
    "Bat": "蝙蝠",
    "Void Bomber": "虚空炸弹",
    "Fire Bomber": "火焰炸弹",
    "Fire Imp": "火焰小鬼",
    "Spark Imp": "电光小鬼",
    "Mind Maggot": "心灵蛆虫",
    "Displacer Beast": "移形兽",
    "Green Mushboom": "绿蘑菇",
    "Mantis": "螳螂",
    "Snake": "蛇",
    "Spriggan": "Spriggan", # 待议
    "Spriggan Bush": "Spriggan Bush",
    "Boggart": "波伽",
    "Orc": "兽人",
    "Pachyderm": "大象",
    "Rotting Zombie": "腐烂僵尸",
    "Ghost": "幽灵",
    "Iron Imp": "铁质小鬼",
    "Satyr": "萨堤尔", # 潘神的追随者 萨堤尔/萨特
    "Large Worm Ball": "大型蠕虫球",
    "Kobold": "狗头人",
    "Witch": "女巫",
    "Rock Worm": "钻地蠕虫",
    "Giant Spider": "巨大蜘蛛",
    "Ice Lizard": "冰蜥蜴",
    "Fire Lizard": "火蜥蜴",
    "Grey Mushboom": "灰蘑菇",
    "Horned Toad": "有角蟾蜍",
    "Raven": "乌鸦",
    "Treant": "树人",
    "Cursed Cat": "被诅咒的猫",
    "Cultist": "邪教徒",
    "Two Headed Snake": "双头蛇",
    "Centaur": "半人马",
    "Ogre": "食人魔",
    "Spore Beast": "孢子兽",
    "Bag of Bugs": "虫子袋", # 袋子自己有行动能力
    "Troll": "巨魔",
    "Troubler": "Troubler", # 待议
    "Evil Faery": "邪恶仙灵",
    "Vampire": "吸血鬼",
    "Vampire Bat": "吸血蝙蝠",
    "Gnome": "地精", # 侏儒地精哥布林傻傻分不清
    "Goatia": "羊头恶魔", # 难听
    "Steel Spider": "钢铁蜘蛛",
    "Green Slime": "绿史莱姆",
    "Polar Bear": "北极熊",
    "Hell Hound": "地狱猎犬",
    "Werewolf": "狼人",
    "Wild Man": "野人",
    "Blizzard Beast": "暴风雪兽",
    "Chaos Chimera": "混沌奇美拉",
    "Fire Lion": "火狮子",
    "Mycobeast": "真菌兽", # Myco-前缀表示和真菌有关
    "Thunderbird": "雷鸟",
    "Bone Knight": "骸骨骑士",
    "Blood Hound": "鲜血猎犬",
    "Spark Spirit": "电光之灵", # 不想叫电光之灵，更不能叫火花之灵
    "Fire Spirit": "火焰之灵",
    "Golem": "魔像",
    "Redcap": "红帽子",
    "Green Gorgon": "绿戈尔贡", # 这玩意不会石化啊，而且也不是人形，它是啥
    "Earth Troll": "大地巨魔",
    "Stonefish": "石鱼", # 鱼，石头做的，还有腿
    "Dancing Blade": "舞蹈的剑",
    "Fire Belcher": "火喷吐者", # 升级版蜥蜴
    "Aether Spider": "以太蜘蛛",
    "Spike Beast": "钉刺兽",
    "Old Witch": "老女巫",
    "Red Slime": "红史莱姆",
    "Ice Slime": "冰史莱姆",
    "Blood Bear": "鲜血熊",
    "Living Scroll of Lightning": "活化闪电卷轴",
    "Living Scroll of Fireball": "活化火球卷轴",
    "Duergar": "灰矮人",
    "Fiery Tormentor": "火热折磨者",
    "Dark Tormentor": "黑暗折磨者",
    "Orc Houndlord": "兽人驯犬师",
    "Warlock": "Warlock", # 战锁，这个效果是招 imp 群然后点化 fiend
    "Void Rift": "虚空裂隙",
    "Flame Rift": "燃烧裂隙", # Flame 换个词吧
    "Rolling Spike Ball": "滚动钉球",
    "Floating Eyeball": "飘浮眼球",
    "Storm Drake": "风暴巨龙",
    "Fire Drake": "火焰巨龙",
    "Bone Shambler": "骸骨跛行者",
    "Worm Shambler": "蠕虫跛行者",
    "Greater Spore Beast": "大孢子兽",
    "Displacer Broodmother": "移形兽母",
    "Mind Maggot Queen": "心灵蛆虫女王",
    "Flame Toad": "燃烧蟾蜍",
    "Void Toad": "虚空蟾蜍",
    "Storm Troll": "风暴巨魔",
    "Minotaur": "牛头人",
    "Greater Vampire": "大吸血鬼",
    "Vampiric Mist": "吸血迷雾",
    "Aelf": "精灵",
    "Ghostly Mass": "幽灵集群",
    "Faery Arcanist": "仙灵奥术师",
    "Purple Hand": "紫色的手",
    "Star Swimmer": "Star Swimmer", # 是个海星
    "Towering Toadbeast": "高大蟾蜍",
    "Deathchill Chimera": "死寒奇美拉",
    "Ice Lion": "冰狮子",
    "Glass Golem": "玻璃魔像",
    "Ice Belcher": "冰喷吐者",
    "Bark Lord": "树皮领主", # 长得很丑的一棵树
    "Starfire Chimera": "星火奇美拉",
    "Star Lion": "星狮子", #是不是有点怪了 TODO
    "Mind Vampire": "心灵吸血鬼",
    "Vampire Eye": "吸血之眼",
    "False Prophet": "伪先知",
    "Mind Devourer": "心灵吞噬者",
    "Fire Wyrm": "火焰游龙", # ……
    "Gargoyle": "石像鬼",
    "Gargoyle Statue": "石像鬼雕塑",
    "Void Slime": "虚空史莱姆",
    "Night Hag": "老鬼婆", # DND
    "Red Cyclops": "红色独眼巨人",
    "Giant Floating Skull": "巨大飘浮头骨",
    "Grey Gorgon": "灰戈尔贡",
    "Efreet": "伊芙利特", # 关键词：火焰、烟雾、精怪、阿拉伯
    "Purple Pachyderm": "紫色大象",
    "Yeti": "雪人",
    "Void Drake": "虚空巨龙",
    "Cockatrice": "鸡蛇兽",
    "Butterfly Demon": "蝴蝶恶魔",
    "Chaos Knight": "混沌骑士",
    "Gold Drake": "黄金巨龙",
    "Flaming Eyeball": "燃烧眼球",
    "Frosty Tormentor": "霜冻折磨者",
    "Giant Spider Queen": "巨大蜘蛛女王",
    "Rotting Mass": "腐烂集群",
    "Dryder": "蛛化精灵", # dnd，其实是蛛化卓尔精灵
    "Dream Hag": "Dream Hag", # 不知道怎么和 Night Hag 协调
    "Ice Drake": "寒冰巨龙",
    "Ice Wyrm": "寒冰游龙", # ……
    "Fire Fiend": "火焰恶魔",
    "Storm Fiend": "风暴恶魔",
    "Iron Fiend": "铁质恶魔",
    "Annihilation Goo": "湮灭黏质", # 什么是 Goo？？有史莱姆词条，有嘴，有不知道是触角还是眼睛
    "Lich": "巫妖",
    "Aelf Lightning Artist": "精灵雷术师",
    "Fae Queen": "仙灵女王",
    "Towering Bone Shambler": "高大骸骨跛行者",
    "Void Knight": "虚空骑士",
    "Storm Knight": "风暴骑士",
    "Nightmare Turtle": "梦魇龟",
    "Lamasu": "拉马苏",
    "Glass Cockatrice": "玻璃鸡蛇兽",
    "Glass Butterfly": "玻璃蝴蝶",
    "Giant Flaming Skull": "巨大燃烧头骨",
    "Phoenix": "凤凰",
    "Steel Spider Queen": "钢铁蜘蛛女王",
    "Aether Spider Queen": "以太蜘蛛女皇",
    "Volcano Turtle": "火山龟",
    "Dracolich": "龙巫妖",
    "Aesir": "亚萨神族", # 亚萨神？
    "Titan": "泰坦",
    "Reaper": "死神",
    "Mass of Eyes": "眼球集群",
    "Fleshy Mass": "血肉集群", # 这个贴图和属性都和巫师招的flesh fiend完全一样
    "Chaos Fiend": "混沌恶魔",
    "Copper Fiend": "铜质恶魔",
    "Furnace Fiend": "熔炉恶魔",
    "Insanity Fiend": "疯狂恶魔",
    "Rot Fiend": "腐烂恶魔",
    "Ash Fiend": "灰烬恶魔",
    "Bone Shambler Megalith": "庞大骸骨跛行者",
    "Golden Skull": "金色颅骨",
    "Energy Knight": "能量骑士",
    "Twilight Knight": "暮光骑士",
    "Watcher": "监视者",
    "Void Watcher": "虚空监视者",
    "Idol of Undeath": "亡灵造像",
    "Fountain of Blood": "鲜血之泉",
    "Fountain of Venom": "毒液之泉",
    "Idol of Insanity": "疯狂造像",
    "Slimesoul Idol": "史莱姆造像",
    "Idol of Agony": "折磨造像",
    "Idol of Frailty": "脆弱造像",
    "Idol of Nightmares": "梦魇造像",
    "Idol of Invincibiity": "无敌造像", # 要不还是叫护盾吧，有什么两个字的词描述无法摧毁的
    "Idol of Fiends": "恶魔造像",
    "Medusa": "美杜莎",
    "Bat Dragon": "蝙蝠龙",
    "Tombstone": "Tombstone", # TODO
    "Yggdrasil": "世界树",
    "Idol of Sorcery": "咒术造像",
    "Time Keeper": "Time Keeper",
    "Giant Soul Jar": "巨型魂匣",
    "Swamp Queen": "沼泽女王",
    "Chaos Quill": "混沌魔笔",
    "Fire Wyrm Egg": "火焰游龙蛋",
    "Ice Wyrm Egg": "冰霜游龙蛋",
    "Box of Woe": "灾祸魔匣", #魔盒？一代叫悲哀盒感觉不太对
    "Bone Wizard": "骸骨巫师",
    "Avian Wizard": "鸟类巫师", # TODO
    "Raven Mage": "乌鸦法师",
    "Lightning Master": "闪电大师",
    "Mountain Mage": "山峦法师",
    "Masked Wizard": "面具巫师",
    "Arachnid Wizard": "蜘蛛巫师", # TODO
    "Dragon Mage": "龙巫师",
    "Troll Geomancer": "巨魔地术师",
    "Void Magus": "Void Magus", # TODO
    "Glass Master": "玻璃大师",
    "Grand Warlock": "Grand Warlock", # TODO
    "Twilight Seer": "暮光先知",
    "Ice Lich": "冰巫妖",
    "Fire Lich": "火巫妖",
    "Ice Wizard": "寒冰巫师",
    "Goblin Wizard": "哥布林巫师",
    "Frostfire Mage": "霜火巫师",
    "Starfire Sorcerer": "星火巫师", # 全部都是巫师（
    "Fire Wizard": "火焰巫师",
    "Enchanter": "附魔师",
    "Troubling Mass": "Troubling Mass", # TODO
    "Vampire Count": "吸血鬼伯爵", # Count是伯爵
    "Black Rider": "饥荒，黑色骑士", # 或者黑之骑士，感觉又很中二
    "White Rider": "瘟疫，白色骑士",
    "Red Rider": "战争，红色骑士",
    "Pale Rider": "瘟疫，青色骑士",
    "The Furnace": "熔炉",
    "Pillar of Bones": "骸骨之柱",
    "Pillar of Worms": "蠕虫之柱",
    "Translocator": "移形师",
    "Mechanomancer": "机械师",
    "Minos, The Golden Bull": "米诺斯，黄金公牛",
    "Chronos, Titan Immortal": "克洛诺斯，不朽泰坦",
    "Odin, Aesir Immortal": "奥丁，不朽亚萨神",
    "Gemini Twin": "双子座",
    "The Mischief Maker": "The Mischief Maker",
    "Slime Drake": "史莱姆巨龙",
    "Void Phoenix": "虚空凤凰",
    "Crucible of Pain": "Crucible of Pain",
    "Idol of Fiery Vengeance": "火热复仇造像",
    "Concussive Idol": "Concussive Idol",
    "Idol of Vampirism": "吸血造像",
    "Bone Colossus": "骸骨巨像",
    "Flesh Colossus": "血肉巨像",
    "Giant Nightmare Turtle": "巨大梦魇龟", #巨型？ 目前 giant 除了魂匣都用的巨大，感觉巨型怪怪的
    "Giant Mass of Eyes": "巨大眼球集群",
    "Giant Gorgon": "巨大戈尔贡",
    "Beastking of Inferno": "Beastking of Inferno",
    "Ultimate Mind Devourer": "究极心灵吞噬者",
    "Giant Sack of Filth": "Giant Sack of Filth",
    "True Lamasu": "真拉马苏",
    "Winterbringer": "凛冬使徒",
    "Moon Mage": "月亮法师",
    "Blood Magus": "鲜血法师",
    "Deathchiller": "Deathchiller",
    "Brain Tree": "脑树",
    "Rot Tree": "腐坏树",
    "Jormungandr": "耶梦加得",
    "Ophan": "座天使",
    "Pope the Frog": "青蛙教皇",
    "Insanity Queen": "疯狂女王",
    "Mordred": "莫德雷德",
}

# 这里是散落在源代码中没有从怪物文件 dump 出来的名字，手动挡
monsters.update({
    "Fire Elemental": "火元素",
    "Starfire Elemental": "星火元素",
    "Golem": "魔像",
    "Flying Golem": "飞行魔像",
    "Skeleton": "骷髅",
    "Flying Skeleton": "飞行骷髅",
    "Wolf": "狼",
    "Ice Hound": "寒冰猎犬",
    "Clay Hound": "黏土猎犬",
    "Giant Bear": "巨熊",
    "Metallic Giant Bear": "金属巨熊",
    "Venom Bear": "毒液熊",
    "Storm Spirit": "风暴之灵",
    "Thorny Plant": "荆棘",
    "Iron Thorn": "铁荆棘",
    "Icy Thorn": "冰荆棘",
    "Orb": "法球",
    "Arcane Orb": "奥术法球",
    "Searing Orb": "灼热法球",
    "Ball Lightning": "球状闪电",
    "Ice Faery": "冰霜仙灵",
    "Frost Eyeball": "霜冻眼球",
})
