def GetBlockset(allowPaint = False):
	FinalSet = {}
	if allowPaint:
		FinalSet.update(PaintBlockset)
	# We override the paint set with the real set because unless my terraria is broken, paint doesn't change the color much	in world
	FinalSet.update(Blockset)
	return FinalSet


# No spreading blocks, only blocks that can free float, placed on background walls or echo blocks
# Technically with these rules this can summon torch god... oh well!
Blockset = {
	(128,128,128) : "Stone Block",
	(73,51,36): "Wooden Beam",
    (200,246,254): "Glass Block",
	(151,107,75): "Wood or Dirt Block",
	(191,142,111): "Platform",
	(253,221,3): "Torch",
	(106,107,118): "Silt",
	(181,62,59): "Brick Block",
	(146,81,68): "Clay Block",
    (190,171,94): "Yellow Stucco",
    (131,162,161): "Green Stucco",
    (170,171,157): "Gray Stucco",
    (239,141,126): "Red Stucco",
    (5,5,5): "Starry Block", # There's blue and gold varients, but they both use the same color
    (202,174,165): "Spider Nest Block",
	# Moss
    (208,0,126): "Argon Moss Brick",
    (254,121,2): "Lava Moss Brick",
    (114,254,2): "Krypton Moss Brick",
    (220,12,237): "Neon Moss Brick",
    (0,197,208): "Xenon Moss Brick",
    # Mechanical
    (240,240,240):"Pixel Box",
    (52,52,52): "Inactive Stone Block",
    (99,255,107): "Logic Gate (AND, OR, or XOR)", # Shouldn't XOR be red as well based on it's sprite? whatever...
    (218,2,5): "Logic Gate (NAND, NOR, or XNOR)",
    (144,148,144): "Dart Trap", # Very suprised this doesn't match stone, Matches venom dart traps though.
    (65,75,90): "Conveyor Belt",
    (50,107,197): "Water Sensor",
    (254,194,20): "Honey Sensor",
    (253,91,3): "Lava Sensor",
    (174,195,215): "Liquid Sensor",
    (185,0,224): "Night Sensor",
    (245,197,1): "Day Sensor",
    (58,240,111): "Player Sensor",
    (60,60,60): "Grate",
	# NPC
	(121,119,101): "Cog",
    (31,31,31): "Smoke Block",
	(251,209,240): "Bubble Block",
    (0,206,180): "Silly Green Balloon",
    (255,66,152): "Silly Pink Balloon",
    (179,132,255): "Silly Purple Balloon",
    (15,15,15): "Midnight Confetti Block",
    (200,246,254): "Confetti Block",
    (151,129,43): "Hay Block", # Collection item is from merchant
    (62,61,52): "Ashphalt Block", # Crafting station is from steampunk
	# Travelling Merchant
	(117,61,25): "Dynasty Wood",
	(204,93,73): "Red Dynasty Shingles",
	(87,150,154): "Blue Dynasty Shingles",
	(165,159,153): "Anti-Portal Block",
	(39,168,96): "Green Team Block",
	(54,183,111): "Green Team Platform",
	(39,94,168): "Blue Team Block",
	(54,109,183): "Blue Team Platform",
	(242,221,100): "Yellow Team Block",
	(255,236,115): "Yellow Team Platform",
	(197,193,216): "White Team Block",
	(212,208,231): "White Team Platform",
	(168,38,47): "Red Team Block",
	(183,53,62): "Red Team Platform",
	(224,100,242): "Pink Team Block",
	(239,115,255): "Pink Team Platform",
	# Christmas
	(192,30,30): "Red Candy Cane",
	(43,192,30): "Green Candy Cane",
	(27,109,69): "Pine Block",
	# Halloween
	(235,150,23): "Pumpkin",
	(57,48,97): "Spooky Wood",
	# Ocean
	(253,227,215): "Shell Pile",
    (198,170,104): "Palm Wood",
    (235,114,80): "Coralstone",
    (235,125,150): "Reef Block",
    (7,51,162): "Waterfall Block",
	# Slime
	(56,121,255): "Slime Block",
	(97,200,255): "Frozen Slime Block",
	(249,101,189): "Pink Slime Block",
	# Mushroom
	(182,175,130): "Glowing Mushroom Block",
	(172,155,110): "Glowing Mushroom Beam",
	# Marble
	(168,178,204): "Marble Block",
    (148,158,184): "Marble Column",
	# Granite
	(50,46,104): "Granite Block",
    (30,26,84): "Granite Column",
	# Dungeon
	(84,100,63): "Green Dungeon Brick",
	(66,84,109): "Blue Dungeon Brick",
	(107,68,99): "Pink Dungeon Brick",
	(157,157,107): "Bone Block",
	#(128,128,128): "Spike Block", # Same as Stone
	# Snow
	(144,195,232): "Ice Block",
	(124,175,201): "Ice Brick",
    (184,219,240): "Thin Ice",
	(96,77,64): "Boreal Wood",
    (76,57,44): "Boreal Wood Beam",
	(211,236,241): "Snow Block",
	(107,132,139): "Slush Block",
    (29,240,255): "Living Frost Fire Block",
    (190,223,232): "Snowfall Block",
	# Sky
	(223,255,255): "Cloud Block",
	(147,144,178): "Raining Cloud Block",
	(213,178,28): "Sunplate Block",
	(55,97,155): "Martian Conduit Plating",
	# Hell
	(68,68,76): "Ash Block",
	(253,62,3): "Living Fire Block",
    (105,74,202): "Living Demon Fire Block",
    (237,29,2): "Lavafall Block",
	(43,40,84): "Obsidian",
	(26,26,26): "Obsidian Brick",
	(142,66,66): "Hellstone Ore or Brick",
    (107,92,108): "Iridescent Brick",
    (145,120,120): "Ashwood",
	# Crimson, No spreading blocks
	(108,34,35): "Crimstone Brick",
	(88,105,118): "Shadewood",
    (254,202,80): "Living Ichor Block",
	(134,22,34): "Flesh Block",
	# Hallow, No spreading blocks
	(238,225,218): "Pearlstone Brick",
    (148,133,98): "Pearlwood",
    (87,21,144): "Crystal Block",
	# Corruption, No spreading blocks
	(104,100,126): "Ebonwood",
	(128,133,184): "Ebonstone Brick",
    (96,248,2): "Living Cursed Flame Block",
	(114,92,95): "Lesion Block",
	# Jungle
	(145,81,85): "Rich Mahogany",
    (125,61,65): "Rich Mahogany Beam",
	(221,136,144): "Living Rich Mahogany",
	(131,206,12): "Living Rich Mahogany Leaves",
	(92,68,73): "Mud Block",
	(255,156,12): "Honey Block",
    (204,124,9): "Honeyfall Block",
	(131,79,13): "Crispy Honey Block",
	(227,125,22): "Hive Block",
	(141,56,0): "Lizhard Brick", # Unsuprisingly, same as the Lizhard traps
	#(145,81,85): "Lizhard Spikes", # Same as Rich Mahogany
	(165,168,26): "Bamboo",
    # Aether
    (247,228,254): "Atherium Block or Brick",
	# Desert
	(178,104,58): "Sandstone Column",
	(186,168,84): "Sand",
	(190,171,94): "Sandstone Brick",
	(198,124,78): "Sandstone",
	(73,120,17): "Cactus Block",
	(255,227,132): "Fossil",
    (211,198,111): "Sandfall Block",
	# Rope
	(137,120,67): "Rope",
	(103,103,103): "Chain",
	(28,216,94): "Vine Rope",
	(223,232,233): "Web Rope",
	(146,136,205): "Silk Rope",
    (92,240,91): "Green Streamer",
    (240,91,147): "Pink Streamer",
    (91,186,240): "Blue Streamer",
	# Lunar Blocks
	(35,200,254): "Stardust Brick",
	(22,173,254): "Stardust Fragment Block",
	(254,158,35): "Solar Brick",
	(249,75,7): "Solar Fragment Block",
	(249,170,236): "Nebula Brick",
	(160,87,234): "Nebula Fragment Block",
	(34,221,151): "Vortex Brick",
	(0,160,170): "Vortex Fragment Block",
	(85,83,82): "Luminite Ore or Brick",
    (40,49,60): "Mercury Brick",
    (21,13,77): "Star Royale Brick",
    (11,67,80): "Cryocore Brick",
    (53,133,103): "Cosmic Ember Brick",
    (195,201,215): "Heavenforge Brick",
    (83,46,57): "Lunar Rust Brick",
    (23,33,81): "Astra Brick",
    (91,87,167): "Dark Celestial Brick",
    # Coins
    (226,118,76): "Copper Coin",
    (161,172,173): "Silver Coin",
    (204,181,72): "Gold Coin",
    (190,190,178): "Platinum Coin",
	# Ore and gems
    (233,180,90): "Amber Ore",
    (110,140,182): "Sapphire Ore",
    (160,118,58): "Topaz Ore",
    (140,58,166): "Amethyst Ore",
    (56,150,97): "Emerald Ore",
    (196,96,114): "Ruby Ore",
    (125,191,197): "Diamond Ore",
	(240,240,247): "Diamond Gemspark Block",
	(255,79,79): "Ruby Gemspark Block",
	(250,255,79): "Topaz Gemspark Block",
	(79,255,89): "Emerald Gemspark Block",
	(79,102,255): "Sapphire Gemspark Block",
	(221,79,255): "Amythest Gemspark Block",
	(255,145,79): "Amber Gemspark Block",
	(224,194,101): "Any Metal Bar",
	(231,96,228): "Orichalcum Ore or Brick",
    (235,38,231): "Bubblegum Block",
	(57,85,101): "Titanium Ore, or Brick",
    (86,85,92): "Titanstone Block",
	(11,80,143): "Cobalt Ore or Brick",
    (128,26,52): "Adamantite Ore or Beam",
    (91,169,169): "Mythril Ore",
    (239,90,50): "Palladium Ore",
	(129,125,93): "Tin Ore or Brick",
    (150,67,22): "Copper Ore, Plating or Brick",
	(62,82,114): "Lead Ore or Brick",
	(185,194,195): "Silver Ore or Brick",
	(132,157,127): "Tungsten Ore or Brick",
	(140,101,80): "Iron Ore or Brick",
	(185,164,23): "Gold Ore or Brick",
	(152,171,198): "Platinum Ore or Brick",
	(98,95,167): "Demonite Ore or Brick",
	(128,55,65): "Crimtane Ore or Brick",
	(104,86,84): "Meteorite Ore or Brick",
	(191,233,115): "Chlorophyte Ore or Brick",
    (44,26,233): "Shroomite Plating"
}




# Fuck the painter, fuck this, im never using paint again.
# If you REALLY want to do this bullshit, go ahead.

PaintBlockset = {
	# Stone Block
    (128,0,0): "Stone Block, Painted Red",
	(128,63,0): "Stone Block, Painted Orange",
	(128,128,0): "Stone Block, Painted Yellow",
	(63,128,0): "Stone Block, Painted Lime",
	(0,128,0): "Stone Block, Painted Green",
	(0,128,63): "Stone Block, Painted Teal",
	(0,128,128): "Stone Block, Painted Cyan",
	(0,63,128): "Stone Block, Painted Sky Blue",
	(0,0,128): "Stone Block, Painted Blue",
	(63,0,128): "Stone Block, Painted Purple",
	(128,0,128): "Stone Block, Painted Violet",
	(128,0,63): "Stone Block, Painted Pink",
	(127,127,127): "Stone Block, Painted Negative",
	(37,37,37): "Stone Block, Painted Black",
	(87,87,87): "Stone Block, Painted Grey",
	# White doesnt change the color, its 128,128,128
	(128,89,62): "Stone Block, Painted Brown",
	(3,3,3): "Stone Block, Painted Shadow",
	# Marble Block
	(204,0,0): "Marble Block, Painted Red",
	(204,101,0): "Marble Block, Painted Orange",
	(204,204,0): "Marble Block, Painted Yellow",
	(101,204,0): "Marble Block, Painted Lime",
	(0,204,0): "Marble Block, Painted Green",
	(0,204,101): "Marble Block, Painted Teal",
	(0,204,204): "Marble Block, Painted Cyan",
	(0,101,204): "Marble Block, Painted Sky Blue",
	(0,0,204): "Marble Block, Painted Blue",
	(101,0,204): "Marble Block, Painted Purple",
	(204,0,204): "Marble Block, Painted Violet",
	(204,0,101): "Marble Block, Painted Pink",
	(87,77,51): "Marble Block, Painted Negative",
	(60,60,60): "Marble Block, Painted Black",
	(140,140,140): "Marble Block, Painted Gray",
	(204,204,204): "Marble Block, Painted White",
	(204,142,100): "Marble Block, Painted Brown",
	(5,5,5): "Marble Block, Painted Shadow",
	# Dirt Block
	(151,0,0): "Dirt or Wood Block, Painted Red",
	(151,75,0): "Dirt or Wood Block, Painted Orange",
	(151,151,0): "Dirt or Wood Block, Painted Yellow",
	(75,151,0): "Dirt or Wood Block, Painted Lime",
	(0,151,0): "Dirt or Wood Block, Painted Green",
	(0,151,75): "Dirt or Wood Block, Painted Teal",
	(0,151,151): "Dirt or Wood Block, Painted Cyan",
	(0,75,151): "Dirt or Wood Block, Painted Sky Blue",
	(0,0,151): "Dirt or Wood Block, Painted Blue",
	(75,0,151): "Dirt or Wood Block, Painted Purple",
	(2,2,2): "Dirt or Wood Block, Painted Shadow"
}