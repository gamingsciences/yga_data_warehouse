// You can find instructions for this file here:
// http://www.treeview.net

// Decide if the names are links or just the icons
USETEXTLINKS = 1  //replace 0 with 1 for hyperlinks

// Decide if the tree is to start all open or just showing the root folders
STARTALLOPEN = 0 //replace 0 with 1 to show the whole tree

ICONPATH = 'Support/' //change if the gif's folder is a subfolder, for example: 'images/'


USEICONS = 1

{
foldersTree = gFld("Title", "title.htm")
foldersTree.iconSrc = ICONPATH + "Gif/globe.gif"
Diag_Node = insFld(foldersTree, gFld("WinOasis", "diagram.htm"))
Diag_Node.iconSrc = ICONPATH + "Gif/ERSTUDIO.gif"
Diag_Node.iconSrcClosed = ICONPATH + "Gif/ERSTUDIO.gif"
Model_Node = insFld(Diag_Node, gFld("Physical", "Content/Model_0e46140543a446ba8053a38c221ebfd9.htm"))
Model_Node.iconSrc = ICONPATH + "Gif/physical.gif"
Model_Node.iconSrcClosed = ICONPATH + "Gif/physical.gif"
{
Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b = insFld(Model_Node, gFld("Main Model", "Content/Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b.htm"))
Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b.iconSrc = ICONPATH + "Gif/grnfldr.gif"
Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b.iconSrcClosed = ICONPATH + "Gif/grnfldr.gif"
EntityFolder = insFld(Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b, gFld("Tables", "Content/Sub_4a16161bf96e4ad2980d2fcb39b7bc8b_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b, gFld("Columns", "Content/Sub_4a16161bf96e4ad2980d2fcb39b7bc8b_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b, gFld("Indexes", "Content/Sub_4a16161bf96e4ad2980d2fcb39b7bc8b_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
ViewFolder = insFld(Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b, gFld("Views", "Content/Sub_4a16161bf96e4ad2980d2fcb39b7bc8b_ViewFrame.htm"))
ViewFolder.iconSrc = ICONPATH + "Gif/viewfldr.gif"
ViewFolder.iconSrcClosed = ICONPATH + "Gif/viewfldr.gif"
RelFolder = insFld(Submodel_4a16161bf96e4ad2980d2fcb39b7bc8b, gFld("Foreign Keys", "Content/Sub_4a16161bf96e4ad2980d2fcb39b7bc8b_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_38c44ca1c77747e6a6d25392ac20fdcd = insFld(Model_Node, gFld("Audit", "Content/Submodel_38c44ca1c77747e6a6d25392ac20fdcd.htm"))
Submodel_38c44ca1c77747e6a6d25392ac20fdcd.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_38c44ca1c77747e6a6d25392ac20fdcd.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_38c44ca1c77747e6a6d25392ac20fdcd, gLnk("R", "Model Image", "Content/Submodel_38c44ca1c77747e6a6d25392ac20fdcd_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_38c44ca1c77747e6a6d25392ac20fdcd, gFld("Tables", "Content/Sub_38c44ca1c77747e6a6d25392ac20fdcd_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_38c44ca1c77747e6a6d25392ac20fdcd, gFld("Columns", "Content/Sub_38c44ca1c77747e6a6d25392ac20fdcd_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_38c44ca1c77747e6a6d25392ac20fdcd, gFld("Indexes", "Content/Sub_38c44ca1c77747e6a6d25392ac20fdcd_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
}
{
Submodel_20569072aeab4fbeb62a122e4a36e510 = insFld(Model_Node, gFld("Bonus Points", "Content/Submodel_20569072aeab4fbeb62a122e4a36e510.htm"))
Submodel_20569072aeab4fbeb62a122e4a36e510.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_20569072aeab4fbeb62a122e4a36e510.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_20569072aeab4fbeb62a122e4a36e510, gLnk("R", "Model Image", "Content/Submodel_20569072aeab4fbeb62a122e4a36e510_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_20569072aeab4fbeb62a122e4a36e510, gFld("Tables", "Content/Sub_20569072aeab4fbeb62a122e4a36e510_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_20569072aeab4fbeb62a122e4a36e510, gFld("Columns", "Content/Sub_20569072aeab4fbeb62a122e4a36e510_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_20569072aeab4fbeb62a122e4a36e510, gFld("Indexes", "Content/Sub_20569072aeab4fbeb62a122e4a36e510_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_20569072aeab4fbeb62a122e4a36e510, gFld("Foreign Keys", "Content/Sub_20569072aeab4fbeb62a122e4a36e510_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_5070325ac6294cb39168c58423098f26 = insFld(Model_Node, gFld("Machine Versioning", "Content/Submodel_5070325ac6294cb39168c58423098f26.htm"))
Submodel_5070325ac6294cb39168c58423098f26.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_5070325ac6294cb39168c58423098f26.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_5070325ac6294cb39168c58423098f26, gLnk("R", "Model Image", "Content/Submodel_5070325ac6294cb39168c58423098f26_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_5070325ac6294cb39168c58423098f26, gFld("Tables", "Content/Sub_5070325ac6294cb39168c58423098f26_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_5070325ac6294cb39168c58423098f26, gFld("Columns", "Content/Sub_5070325ac6294cb39168c58423098f26_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_5070325ac6294cb39168c58423098f26, gFld("Indexes", "Content/Sub_5070325ac6294cb39168c58423098f26_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_5070325ac6294cb39168c58423098f26, gFld("Foreign Keys", "Content/Sub_5070325ac6294cb39168c58423098f26_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_8dd251396e604dfb8f1f1dbf842455ba = insFld(Model_Node, gFld("Marketing Manager", "Content/Submodel_8dd251396e604dfb8f1f1dbf842455ba.htm"))
Submodel_8dd251396e604dfb8f1f1dbf842455ba.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_8dd251396e604dfb8f1f1dbf842455ba.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_8dd251396e604dfb8f1f1dbf842455ba, gLnk("R", "Model Image", "Content/Submodel_8dd251396e604dfb8f1f1dbf842455ba_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_8dd251396e604dfb8f1f1dbf842455ba, gFld("Tables", "Content/Sub_8dd251396e604dfb8f1f1dbf842455ba_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_8dd251396e604dfb8f1f1dbf842455ba, gFld("Columns", "Content/Sub_8dd251396e604dfb8f1f1dbf842455ba_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_8dd251396e604dfb8f1f1dbf842455ba, gFld("Indexes", "Content/Sub_8dd251396e604dfb8f1f1dbf842455ba_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
ViewFolder = insFld(Submodel_8dd251396e604dfb8f1f1dbf842455ba, gFld("Views", "Content/Sub_8dd251396e604dfb8f1f1dbf842455ba_ViewFrame.htm"))
ViewFolder.iconSrc = ICONPATH + "Gif/viewfldr.gif"
ViewFolder.iconSrcClosed = ICONPATH + "Gif/viewfldr.gif"
RelFolder = insFld(Submodel_8dd251396e604dfb8f1f1dbf842455ba, gFld("Foreign Keys", "Content/Sub_8dd251396e604dfb8f1f1dbf842455ba_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_d28edb1b26774ac9ad77f97f93300935 = insFld(Model_Node, gFld("nTime", "Content/Submodel_d28edb1b26774ac9ad77f97f93300935.htm"))
Submodel_d28edb1b26774ac9ad77f97f93300935.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_d28edb1b26774ac9ad77f97f93300935.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_d28edb1b26774ac9ad77f97f93300935, gLnk("R", "Model Image", "Content/Submodel_d28edb1b26774ac9ad77f97f93300935_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_d28edb1b26774ac9ad77f97f93300935, gFld("Tables", "Content/Sub_d28edb1b26774ac9ad77f97f93300935_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_d28edb1b26774ac9ad77f97f93300935, gFld("Columns", "Content/Sub_d28edb1b26774ac9ad77f97f93300935_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_d28edb1b26774ac9ad77f97f93300935, gFld("Indexes", "Content/Sub_d28edb1b26774ac9ad77f97f93300935_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_d28edb1b26774ac9ad77f97f93300935, gFld("Foreign Keys", "Content/Sub_d28edb1b26774ac9ad77f97f93300935_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003 = insFld(Model_Node, gFld("Patron Groups", "Content/Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003.htm"))
Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003, gLnk("R", "Model Image", "Content/Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003, gFld("Tables", "Content/Sub_e93aa7e9b6bf42a6b5dcd7464af1b003_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003, gFld("Columns", "Content/Sub_e93aa7e9b6bf42a6b5dcd7464af1b003_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003, gFld("Indexes", "Content/Sub_e93aa7e9b6bf42a6b5dcd7464af1b003_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_e93aa7e9b6bf42a6b5dcd7464af1b003, gFld("Foreign Keys", "Content/Sub_e93aa7e9b6bf42a6b5dcd7464af1b003_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_e4adb233f0ec4424a60e66cfca388965 = insFld(Model_Node, gFld("Personal Banker", "Content/Submodel_e4adb233f0ec4424a60e66cfca388965.htm"))
Submodel_e4adb233f0ec4424a60e66cfca388965.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_e4adb233f0ec4424a60e66cfca388965.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_e4adb233f0ec4424a60e66cfca388965, gLnk("R", "Model Image", "Content/Submodel_e4adb233f0ec4424a60e66cfca388965_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_e4adb233f0ec4424a60e66cfca388965, gFld("Tables", "Content/Sub_e4adb233f0ec4424a60e66cfca388965_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_e4adb233f0ec4424a60e66cfca388965, gFld("Columns", "Content/Sub_e4adb233f0ec4424a60e66cfca388965_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_e4adb233f0ec4424a60e66cfca388965, gFld("Indexes", "Content/Sub_e4adb233f0ec4424a60e66cfca388965_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
}
{
Submodel_e14d4911bf34458b8ccc18d36fec6e8e = insFld(Model_Node, gFld("Player", "Content/Submodel_e14d4911bf34458b8ccc18d36fec6e8e.htm"))
Submodel_e14d4911bf34458b8ccc18d36fec6e8e.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_e14d4911bf34458b8ccc18d36fec6e8e.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_e14d4911bf34458b8ccc18d36fec6e8e, gLnk("R", "Model Image", "Content/Submodel_e14d4911bf34458b8ccc18d36fec6e8e_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_e14d4911bf34458b8ccc18d36fec6e8e, gFld("Tables", "Content/Sub_e14d4911bf34458b8ccc18d36fec6e8e_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_e14d4911bf34458b8ccc18d36fec6e8e, gFld("Columns", "Content/Sub_e14d4911bf34458b8ccc18d36fec6e8e_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_e14d4911bf34458b8ccc18d36fec6e8e, gFld("Indexes", "Content/Sub_e14d4911bf34458b8ccc18d36fec6e8e_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_e14d4911bf34458b8ccc18d36fec6e8e, gFld("Foreign Keys", "Content/Sub_e14d4911bf34458b8ccc18d36fec6e8e_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_054f76fd30864e71895bcfa43cf894fc = insFld(Model_Node, gFld("Player Statistics", "Content/Submodel_054f76fd30864e71895bcfa43cf894fc.htm"))
Submodel_054f76fd30864e71895bcfa43cf894fc.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_054f76fd30864e71895bcfa43cf894fc.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_054f76fd30864e71895bcfa43cf894fc, gLnk("R", "Model Image", "Content/Submodel_054f76fd30864e71895bcfa43cf894fc_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_054f76fd30864e71895bcfa43cf894fc, gFld("Tables", "Content/Sub_054f76fd30864e71895bcfa43cf894fc_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_054f76fd30864e71895bcfa43cf894fc, gFld("Columns", "Content/Sub_054f76fd30864e71895bcfa43cf894fc_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_054f76fd30864e71895bcfa43cf894fc, gFld("Indexes", "Content/Sub_054f76fd30864e71895bcfa43cf894fc_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
ViewFolder = insFld(Submodel_054f76fd30864e71895bcfa43cf894fc, gFld("Views", "Content/Sub_054f76fd30864e71895bcfa43cf894fc_ViewFrame.htm"))
ViewFolder.iconSrc = ICONPATH + "Gif/viewfldr.gif"
ViewFolder.iconSrcClosed = ICONPATH + "Gif/viewfldr.gif"
RelFolder = insFld(Submodel_054f76fd30864e71895bcfa43cf894fc, gFld("Foreign Keys", "Content/Sub_054f76fd30864e71895bcfa43cf894fc_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_0b7b7320375748a8bd576c04f7f67731 = insFld(Model_Node, gFld("Progressive Links", "Content/Submodel_0b7b7320375748a8bd576c04f7f67731.htm"))
Submodel_0b7b7320375748a8bd576c04f7f67731.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_0b7b7320375748a8bd576c04f7f67731.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_0b7b7320375748a8bd576c04f7f67731, gLnk("R", "Model Image", "Content/Submodel_0b7b7320375748a8bd576c04f7f67731_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_0b7b7320375748a8bd576c04f7f67731, gFld("Tables", "Content/Sub_0b7b7320375748a8bd576c04f7f67731_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_0b7b7320375748a8bd576c04f7f67731, gFld("Columns", "Content/Sub_0b7b7320375748a8bd576c04f7f67731_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_0b7b7320375748a8bd576c04f7f67731, gFld("Indexes", "Content/Sub_0b7b7320375748a8bd576c04f7f67731_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
}
{
Submodel_062be55b77ef4bf7b666bebbc03f6f50 = insFld(Model_Node, gFld("Rating", "Content/Submodel_062be55b77ef4bf7b666bebbc03f6f50.htm"))
Submodel_062be55b77ef4bf7b666bebbc03f6f50.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_062be55b77ef4bf7b666bebbc03f6f50.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_062be55b77ef4bf7b666bebbc03f6f50, gLnk("R", "Model Image", "Content/Submodel_062be55b77ef4bf7b666bebbc03f6f50_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_062be55b77ef4bf7b666bebbc03f6f50, gFld("Tables", "Content/Sub_062be55b77ef4bf7b666bebbc03f6f50_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_062be55b77ef4bf7b666bebbc03f6f50, gFld("Columns", "Content/Sub_062be55b77ef4bf7b666bebbc03f6f50_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_062be55b77ef4bf7b666bebbc03f6f50, gFld("Indexes", "Content/Sub_062be55b77ef4bf7b666bebbc03f6f50_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
}
{
Submodel_10b0b38fec844e2cbc70f469f531c40f = insFld(Model_Node, gFld("SchedulerService", "Content/Submodel_10b0b38fec844e2cbc70f469f531c40f.htm"))
Submodel_10b0b38fec844e2cbc70f469f531c40f.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_10b0b38fec844e2cbc70f469f531c40f.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_10b0b38fec844e2cbc70f469f531c40f, gLnk("R", "Model Image", "Content/Submodel_10b0b38fec844e2cbc70f469f531c40f_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_10b0b38fec844e2cbc70f469f531c40f, gFld("Tables", "Content/Sub_10b0b38fec844e2cbc70f469f531c40f_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_10b0b38fec844e2cbc70f469f531c40f, gFld("Columns", "Content/Sub_10b0b38fec844e2cbc70f469f531c40f_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_10b0b38fec844e2cbc70f469f531c40f, gFld("Indexes", "Content/Sub_10b0b38fec844e2cbc70f469f531c40f_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_10b0b38fec844e2cbc70f469f531c40f, gFld("Foreign Keys", "Content/Sub_10b0b38fec844e2cbc70f469f531c40f_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_6f3e4ad7aae64e3db9f0421b25309dc8 = insFld(Model_Node, gFld("Security", "Content/Submodel_6f3e4ad7aae64e3db9f0421b25309dc8.htm"))
Submodel_6f3e4ad7aae64e3db9f0421b25309dc8.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_6f3e4ad7aae64e3db9f0421b25309dc8.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_6f3e4ad7aae64e3db9f0421b25309dc8, gLnk("R", "Model Image", "Content/Submodel_6f3e4ad7aae64e3db9f0421b25309dc8_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_6f3e4ad7aae64e3db9f0421b25309dc8, gFld("Tables", "Content/Sub_6f3e4ad7aae64e3db9f0421b25309dc8_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_6f3e4ad7aae64e3db9f0421b25309dc8, gFld("Columns", "Content/Sub_6f3e4ad7aae64e3db9f0421b25309dc8_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_6f3e4ad7aae64e3db9f0421b25309dc8, gFld("Indexes", "Content/Sub_6f3e4ad7aae64e3db9f0421b25309dc8_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_6f3e4ad7aae64e3db9f0421b25309dc8, gFld("Foreign Keys", "Content/Sub_6f3e4ad7aae64e3db9f0421b25309dc8_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62 = insFld(Model_Node, gFld("Slot Revenue", "Content/Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62.htm"))
Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62, gLnk("R", "Model Image", "Content/Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62, gFld("Tables", "Content/Sub_e5e1ad9027c04ce5a9b4e2aef2089f62_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62, gFld("Columns", "Content/Sub_e5e1ad9027c04ce5a9b4e2aef2089f62_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_e5e1ad9027c04ce5a9b4e2aef2089f62, gFld("Indexes", "Content/Sub_e5e1ad9027c04ce5a9b4e2aef2089f62_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
}
{
Submodel_0313b757d569475992f7b1d3b1fc4950 = insFld(Model_Node, gFld("SpeedMedia", "Content/Submodel_0313b757d569475992f7b1d3b1fc4950.htm"))
Submodel_0313b757d569475992f7b1d3b1fc4950.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_0313b757d569475992f7b1d3b1fc4950.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_0313b757d569475992f7b1d3b1fc4950, gLnk("R", "Model Image", "Content/Submodel_0313b757d569475992f7b1d3b1fc4950_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_0313b757d569475992f7b1d3b1fc4950, gFld("Tables", "Content/Sub_0313b757d569475992f7b1d3b1fc4950_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_0313b757d569475992f7b1d3b1fc4950, gFld("Columns", "Content/Sub_0313b757d569475992f7b1d3b1fc4950_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_0313b757d569475992f7b1d3b1fc4950, gFld("Indexes", "Content/Sub_0313b757d569475992f7b1d3b1fc4950_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_0313b757d569475992f7b1d3b1fc4950, gFld("Foreign Keys", "Content/Sub_0313b757d569475992f7b1d3b1fc4950_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_48c5c467a3ae475f8ce018a1672f6f38 = insFld(Model_Node, gFld("SpeedMedia Campaigns", "Content/Submodel_48c5c467a3ae475f8ce018a1672f6f38.htm"))
Submodel_48c5c467a3ae475f8ce018a1672f6f38.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_48c5c467a3ae475f8ce018a1672f6f38.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_48c5c467a3ae475f8ce018a1672f6f38, gLnk("R", "Model Image", "Content/Submodel_48c5c467a3ae475f8ce018a1672f6f38_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_48c5c467a3ae475f8ce018a1672f6f38, gFld("Tables", "Content/Sub_48c5c467a3ae475f8ce018a1672f6f38_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_48c5c467a3ae475f8ce018a1672f6f38, gFld("Columns", "Content/Sub_48c5c467a3ae475f8ce018a1672f6f38_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_48c5c467a3ae475f8ce018a1672f6f38, gFld("Indexes", "Content/Sub_48c5c467a3ae475f8ce018a1672f6f38_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_48c5c467a3ae475f8ce018a1672f6f38, gFld("Foreign Keys", "Content/Sub_48c5c467a3ae475f8ce018a1672f6f38_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_568c277687994137965ab10cb028ac96 = insFld(Model_Node, gFld("SpeedMedia Events", "Content/Submodel_568c277687994137965ab10cb028ac96.htm"))
Submodel_568c277687994137965ab10cb028ac96.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_568c277687994137965ab10cb028ac96.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_568c277687994137965ab10cb028ac96, gLnk("R", "Model Image", "Content/Submodel_568c277687994137965ab10cb028ac96_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_568c277687994137965ab10cb028ac96, gFld("Tables", "Content/Sub_568c277687994137965ab10cb028ac96_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_568c277687994137965ab10cb028ac96, gFld("Columns", "Content/Sub_568c277687994137965ab10cb028ac96_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_568c277687994137965ab10cb028ac96, gFld("Indexes", "Content/Sub_568c277687994137965ab10cb028ac96_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_568c277687994137965ab10cb028ac96, gFld("Foreign Keys", "Content/Sub_568c277687994137965ab10cb028ac96_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb = insFld(Model_Node, gFld("SpeedMedia Play 'n Win", "Content/Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb.htm"))
Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb, gLnk("R", "Model Image", "Content/Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb, gFld("Tables", "Content/Sub_e30999e4d8dc4ee08fa9a2fb5f0134eb_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb, gFld("Columns", "Content/Sub_e30999e4d8dc4ee08fa9a2fb5f0134eb_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb, gFld("Indexes", "Content/Sub_e30999e4d8dc4ee08fa9a2fb5f0134eb_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_e30999e4d8dc4ee08fa9a2fb5f0134eb, gFld("Foreign Keys", "Content/Sub_e30999e4d8dc4ee08fa9a2fb5f0134eb_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_3fa5b5494e9346a1a52c1dd66a795e31 = insFld(Model_Node, gFld("Tiered Ranks", "Content/Submodel_3fa5b5494e9346a1a52c1dd66a795e31.htm"))
Submodel_3fa5b5494e9346a1a52c1dd66a795e31.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_3fa5b5494e9346a1a52c1dd66a795e31.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_3fa5b5494e9346a1a52c1dd66a795e31, gLnk("R", "Model Image", "Content/Submodel_3fa5b5494e9346a1a52c1dd66a795e31_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_3fa5b5494e9346a1a52c1dd66a795e31, gFld("Tables", "Content/Sub_3fa5b5494e9346a1a52c1dd66a795e31_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_3fa5b5494e9346a1a52c1dd66a795e31, gFld("Columns", "Content/Sub_3fa5b5494e9346a1a52c1dd66a795e31_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_3fa5b5494e9346a1a52c1dd66a795e31, gFld("Indexes", "Content/Sub_3fa5b5494e9346a1a52c1dd66a795e31_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_3fa5b5494e9346a1a52c1dd66a795e31, gFld("Foreign Keys", "Content/Sub_3fa5b5494e9346a1a52c1dd66a795e31_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_930d97cf940f436fa698b6c1fdd20c87 = insFld(Model_Node, gFld("Util", "Content/Submodel_930d97cf940f436fa698b6c1fdd20c87.htm"))
Submodel_930d97cf940f436fa698b6c1fdd20c87.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_930d97cf940f436fa698b6c1fdd20c87.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_930d97cf940f436fa698b6c1fdd20c87, gLnk("R", "Model Image", "Content/Submodel_930d97cf940f436fa698b6c1fdd20c87_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_930d97cf940f436fa698b6c1fdd20c87, gFld("Tables", "Content/Sub_930d97cf940f436fa698b6c1fdd20c87_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_930d97cf940f436fa698b6c1fdd20c87, gFld("Columns", "Content/Sub_930d97cf940f436fa698b6c1fdd20c87_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_930d97cf940f436fa698b6c1fdd20c87, gFld("Indexes", "Content/Sub_930d97cf940f436fa698b6c1fdd20c87_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_930d97cf940f436fa698b6c1fdd20c87, gFld("Foreign Keys", "Content/Sub_930d97cf940f436fa698b6c1fdd20c87_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_7872adaea2fa4125825fd2348853e9cd = insFld(Model_Node, gFld("Voyage", "Content/Submodel_7872adaea2fa4125825fd2348853e9cd.htm"))
Submodel_7872adaea2fa4125825fd2348853e9cd.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_7872adaea2fa4125825fd2348853e9cd.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_7872adaea2fa4125825fd2348853e9cd, gLnk("R", "Model Image", "Content/Submodel_7872adaea2fa4125825fd2348853e9cd_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_7872adaea2fa4125825fd2348853e9cd, gFld("Tables", "Content/Sub_7872adaea2fa4125825fd2348853e9cd_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_7872adaea2fa4125825fd2348853e9cd, gFld("Columns", "Content/Sub_7872adaea2fa4125825fd2348853e9cd_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_7872adaea2fa4125825fd2348853e9cd, gFld("Indexes", "Content/Sub_7872adaea2fa4125825fd2348853e9cd_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
RelFolder = insFld(Submodel_7872adaea2fa4125825fd2348853e9cd, gFld("Foreign Keys", "Content/Sub_7872adaea2fa4125825fd2348853e9cd_RelFrame.htm"))
RelFolder.iconSrc = ICONPATH + "Gif/relfldr.gif"
RelFolder.iconSrcClosed = ICONPATH + "Gif/relfldr.gif"
}
{
Submodel_2432d9a334a846a19f34665521dacc2c = insFld(Model_Node, gFld("Watchdog", "Content/Submodel_2432d9a334a846a19f34665521dacc2c.htm"))
Submodel_2432d9a334a846a19f34665521dacc2c.iconSrc = ICONPATH + "Gif/subphys.gif"
Submodel_2432d9a334a846a19f34665521dacc2c.iconSrcClosed = ICONPATH + "Gif/subphys.gif"
SubmodelImgNode = insDoc(Submodel_2432d9a334a846a19f34665521dacc2c, gLnk("R", "Model Image", "Content/Submodel_2432d9a334a846a19f34665521dacc2c_img.htm"))
SubmodelImgNode.iconSrc = ICONPATH + "Gif/image.gif"
SubmodelImgNode.altTxt = "Model Image"
EntityFolder = insFld(Submodel_2432d9a334a846a19f34665521dacc2c, gFld("Tables", "Content/Sub_2432d9a334a846a19f34665521dacc2c_EntFrame.htm"))
EntityFolder.iconSrc = ICONPATH + "Gif/entfldr.gif"
EntityFolder.iconSrcClosed = ICONPATH + "Gif/entfldr.gif"
AttrFolder = insFld(Submodel_2432d9a334a846a19f34665521dacc2c, gFld("Columns", "Content/Sub_2432d9a334a846a19f34665521dacc2c_AttrFrame.htm"))
AttrFolder.iconSrc = ICONPATH + "Gif/attr.gif"
AttrFolder.iconSrcClosed = ICONPATH + "Gif/attr.gif"
IndexFolder = insFld(Submodel_2432d9a334a846a19f34665521dacc2c, gFld("Indexes", "Content/Sub_2432d9a334a846a19f34665521dacc2c_IdxFrame.htm"))
IndexFolder.iconSrc = ICONPATH + "Gif/index.gif"
IndexFolder.iconSrcClosed = ICONPATH + "Gif/index.gif"
}
}
